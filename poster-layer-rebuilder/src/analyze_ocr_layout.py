from pathlib import Path
import argparse
import json

import cv2
import numpy as np
import pytesseract
from PIL import Image


def detect_color_regions(image_path):
    bgr = cv2.imread(str(image_path))
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    masks = {
        'blue': cv2.inRange(hsv, (95, 60, 70), (125, 255, 255)),
        'green': cv2.inRange(hsv, (40, 50, 70), (85, 255, 255)),
        'orange_yellow': cv2.inRange(hsv, (10, 70, 100), (38, 255, 255)),
        'purple': cv2.inRange(hsv, (125, 50, 70), (160, 255, 255)),
    }
    red1 = cv2.inRange(hsv, (0, 70, 80), (10, 255, 255))
    red2 = cv2.inRange(hsv, (170, 70, 80), (180, 255, 255))
    masks['red'] = cv2.bitwise_or(red1, red2)

    items = []
    kernel = np.ones((3, 3), np.uint8)
    for color_name, mask in masks.items():
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            area = float(cv2.contourArea(contour))
            if area >= 45 and w >= 5 and h >= 5:
                items.append({'type': 'color_region', 'color': color_name, 'box': [int(x), int(y), int(w), int(h)], 'area': area})
    return sorted(items, key=lambda item: (item['box'][1], item['box'][0]))


def run_ocr(image_path):
    img = Image.open(image_path).convert('RGB')
    data = pytesseract.image_to_data(img, lang='vie+eng', config='--psm 6', output_type=pytesseract.Output.DICT)
    lines = {}
    for i, text in enumerate(data['text']):
        text = (text or '').strip()
        if not text:
            continue
        try:
            conf = float(data['conf'][i])
        except Exception:
            conf = -1
        if conf < 30:
            continue
        key = (data['block_num'][i], data['par_num'][i], data['line_num'][i])
        x = int(data['left'][i]); y = int(data['top'][i]); w = int(data['width'][i]); h = int(data['height'][i])
        if key not in lines:
            lines[key] = {'words': [], 'box': [x, y, x + w, y + h], 'confidence': []}
        lines[key]['words'].append(text)
        box = lines[key]['box']
        box[0] = min(box[0], x); box[1] = min(box[1], y)
        box[2] = max(box[2], x + w); box[3] = max(box[3], y + h)
        lines[key]['confidence'].append(conf)

    result = []
    for item in lines.values():
        x1, y1, x2, y2 = item['box']
        text = ' '.join(item['words'])
        if len(text) >= 2:
            result.append({
                'type': 'ocr_text_line',
                'text': text,
                'box': [x1, y1, x2 - x1, y2 - y1],
                'confidence': round(sum(item['confidence']) / len(item['confidence']), 2)
            })
    return sorted(result, key=lambda item: (item['box'][1], item['box'][0]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_image')
    parser.add_argument('--out', default='dist/auto-analysis.json')
    args = parser.parse_args()

    image_path = Path(args.input_image)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    report = {
        'input_image': str(image_path),
        'ocr_text_lines': run_ocr(image_path),
        'detected_color_regions': detect_color_regions(image_path)
    }
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Done:', out_path)


if __name__ == '__main__':
    main()
