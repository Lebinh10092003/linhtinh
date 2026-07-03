from pathlib import Path
import json
import argparse
from PIL import Image, ImageEnhance, ImageFilter


def safe_name(text):
    return ''.join(c if c.isalnum() or c in '-_.' else '_' for c in text)


def crop_box(img, box):
    x, y, w, h = box
    return img.crop((x, y, x + w, y + h))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_image')
    parser.add_argument('--blueprint', default='blueprints/nguyen_du_poster.json')
    parser.add_argument('--out', default='dist')
    parser.add_argument('--layers', default='layers')
    args = parser.parse_args()

    input_path = Path(args.input_image)
    out_dir = Path(args.out)
    layers_dir = Path(args.layers)
    out_dir.mkdir(parents=True, exist_ok=True)
    layers_dir.mkdir(parents=True, exist_ok=True)

    blueprint = json.loads(Path(args.blueprint).read_text(encoding='utf-8'))
    img = Image.open(input_path).convert('RGB')

    exported = []
    for index, layer in enumerate(blueprint['layers']):
        file_name = f'{index:02d}_{safe_name(layer["id"])}.png'
        crop_box(img, layer['box']).save(layers_dir / file_name, optimize=True)
        item = dict(layer)
        item['file'] = file_name
        exported.append(item)

    w, h = img.size
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">']
    svg.append('<rect id="white_background" width="100%" height="100%" fill="#ffffff"/>')
    for layer in exported:
        x, y, lw, lh = layer['box']
        svg.append(f'<g id="{layer["id"]}"><image href="../layers/{layer["file"]}" x="{x}" y="{y}" width="{lw}" height="{lh}" preserveAspectRatio="none"/></g>')
    svg.append('</svg>')
    (out_dir / 'poster-layered-linked.svg').write_text('\n'.join(svg), encoding='utf-8')

    a4 = img.resize((2480, 3508), Image.Resampling.LANCZOS)
    a4 = a4.filter(ImageFilter.UnsharpMask(radius=1.0, percent=110, threshold=3))
    a4 = ImageEnhance.Sharpness(a4).enhance(1.04)
    a4.save(out_dir / 'poster-print-a4-300dpi.png', dpi=(300, 300), optimize=True)
    a4.save(out_dir / 'poster-print-a4-300dpi.jpg', quality=96, dpi=(300, 300), optimize=True, progressive=True)
    a4.save(out_dir / 'poster-print-a4-300dpi.pdf', 'PDF', resolution=300.0)

    report = {
        'input_image': str(input_path),
        'image_size': list(img.size),
        'layers': exported,
        'outputs': ['poster-layered-linked.svg', 'poster-print-a4-300dpi.pdf', 'poster-print-a4-300dpi.png', 'poster-print-a4-300dpi.jpg']
    }
    (out_dir / 'layers.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Done:', out_dir)


if __name__ == '__main__':
    main()
