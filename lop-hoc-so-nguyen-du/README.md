# Poster lớp học số - THCS Nguyễn Du

Bộ file này dựng lại poster theo hướng **code-based editable**: có thể sửa chữ, màu, bố cục bằng SVG/HTML/Python và xuất lại ảnh PNG.

## File chính

- `index.html`: mở trực tiếp trên trình duyệt, xem poster và bấm tải SVG/PNG.
- `dist/lop-hoc-so-nguyen-du.svg`: bản thiết kế dạng vector, sửa được bằng Figma, Illustrator, Inkscape hoặc chỉnh trực tiếp trong code.
- `dist/lop-hoc-so-nguyen-du.png`: ảnh đã xuất sẵn.
- `src/render_poster.py`: mã nguồn tạo lại SVG và PNG.
- `assets/original-reference.png`: ảnh gốc dùng làm tham chiếu.

## Cách sửa nhanh

1. Mở `dist/lop-hoc-so-nguyen-du.svg` bằng Figma/Inkscape để sửa trực quan.
2. Hoặc sửa trực tiếp nội dung trong `src/render_poster.py`.
3. Chạy lại:

```bash
pip install -r requirements.txt
python src/render_poster.py
```

Sau khi chạy, file mới sẽ được xuất ra thư mục `dist/`.

## Ghi chú

Thiết kế này là bản dựng lại bằng vector và code, không phải chuyển tự động từ ảnh gốc sang layer 100%. Vì vậy phần ảnh người thật trong poster gốc được thay bằng minh họa vector để dễ chỉnh sửa và xuất ảnh ổn định.
