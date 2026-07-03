# Raster to Layered Poster - THCS Nguyễn Du

Công cụ này nhận ảnh poster mẫu đầu vào, phân tích lại bố cục và xuất ra nhiều định dạng phục vụ chỉnh sửa/in ấn:

- `dist/poster-print-a4-300dpi.pdf`: bản PDF A4 300DPI để in.
- `dist/poster-print-a4-300dpi.png`: bản PNG A4 300DPI.
- `dist/poster-layered-linked.svg`: SVG có các layer ảnh/crop theo từng khối, dễ import vào Figma/Inkscape.
- `dist/poster-layered-embedded.svg`: SVG nhúng ảnh, tiện kéo thả/import.
- `dist/poster-ocr-editable-text.svg`: lớp chữ OCR dạng text có thể sửa, dùng làm nền để dựng lại chữ.
- `dist/poster-layered.psd`: PSD nhiều layer dạng ảnh/crop, có thể mở bằng Photoshop/Photopea.
- `dist/layers.json`: tọa độ, loại layer, vùng OCR, vùng màu phát hiện.
- `layers/*.png`: từng layer/crop riêng lẻ.

## Cách chạy

```bash
pip install pillow opencv-python pytesseract numpy
python src/reconstruct_poster.py input/poster-original.png --out dist --layers layers --blueprint blueprints/nguyen_du_poster.json
```

Máy cần cài thêm Tesseract OCR nếu muốn xuất lớp chữ OCR. Trên Ubuntu có thể dùng:

```bash
sudo apt install tesseract-ocr tesseract-ocr-vie
```

## Cách đưa vào Figma

1. Mở Figma.
2. Kéo file `dist/poster-layered-embedded.svg` vào canvas.
3. Figma sẽ giữ các group/layer theo ID SVG ở mức tốt nhất có thể.
4. Dùng `poster-ocr-editable-text.svg` để lấy lớp chữ OCR nếu cần dựng lại text.

## Giới hạn kỹ thuật

Từ một ảnh phẳng PNG/JPG, không thể khôi phục 100% file gốc Photoshop/Figma với font, ảnh, icon vector và layer ban đầu. Công cụ này dùng cách gần thực tế nhất:

1. Giữ độ giống mẫu bằng cách tách ảnh gốc thành nhiều layer/crop.
2. Nhận diện layout bằng blueprint + thuật toán phát hiện vùng màu.
3. Nhận diện chữ bằng OCR và xuất thành lớp text có thể sửa.
4. Xuất bản in A4 300DPI để in rõ nét.

Muốn sửa từng chữ/icon chính xác như file gốc, cần dựng lại thủ công dựa trên các layer và OCR này, hoặc cần file Canva/Figma/PSD gốc.
