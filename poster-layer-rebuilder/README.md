# Raster to Layered Poster - THCS Nguyễn Du

Công cụ này nhận ảnh poster mẫu đầu vào, phân tích lại bố cục và xuất ra nhiều định dạng phục vụ chỉnh sửa/in ấn.

## Đầu ra chính

- `dist/poster-print-a4-300dpi.pdf`: bản PDF A4 300DPI để in.
- `dist/poster-print-a4-300dpi.png`: bản PNG A4 300DPI.
- `dist/poster-layered-linked.svg`: SVG có các layer ảnh/crop theo từng khối, dễ import vào Figma/Inkscape.
- `dist/layers.json`: tọa độ layer/crop.
- `layers/*.png`: từng layer/crop riêng lẻ.
- `dist/auto-analysis.json`: kết quả OCR và các vùng màu phát hiện tự động.

Bản ZIP do ChatGPT xuất sẵn có thêm `poster-layered-embedded.svg`, `poster-ocr-editable-text.svg` và `poster-layered.psd`.

## Cách chạy

```bash
pip install pillow opencv-python pytesseract numpy
python src/reconstruct_poster_min.py input/poster-original.png --out dist --layers layers --blueprint blueprints/nguyen_du_poster.json
python src/analyze_ocr_layout.py input/poster-original.png --out dist/auto-analysis.json
```

Máy cần cài thêm Tesseract OCR nếu muốn phân tích chữ. Trên Ubuntu có thể dùng:

```bash
sudo apt install tesseract-ocr tesseract-ocr-vie
```

## Cách đưa vào Figma

1. Chạy script để tạo `dist/poster-layered-linked.svg` và thư mục `layers/`.
2. Mở SVG bằng Inkscape hoặc kéo vào Figma.
3. Các group/layer được đặt ID theo từng khối: logo, tiêu đề, ảnh hero, từng card, app row, benefit block, footer.
4. Dùng kết quả OCR trong `auto-analysis.json` để dựng lại lớp chữ có thể chỉnh sửa.

## Giới hạn kỹ thuật

Từ một ảnh phẳng PNG/JPG, không thể khôi phục 100% file gốc Photoshop/Figma với font, ảnh, icon vector và layer ban đầu. Công cụ này dùng cách gần thực tế nhất:

1. Giữ độ giống mẫu bằng cách tách ảnh gốc thành nhiều layer/crop.
2. Nhận diện layout bằng blueprint + thuật toán phát hiện vùng màu.
3. Nhận diện chữ bằng OCR để hỗ trợ dựng lại text.
4. Xuất bản in A4 300DPI để in rõ nét.

Muốn sửa từng chữ/icon chính xác như file gốc, cần dựng lại thủ công dựa trên các layer và OCR này, hoặc cần file Canva/Figma/PSD gốc.
