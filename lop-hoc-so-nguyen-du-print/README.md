# Poster lớp học số - THCS Nguyễn Du - bản đúng mẫu và bản in

Bộ file này dùng chính ảnh mẫu làm nguồn để hiển thị giống mẫu nhất có thể, đồng thời có công cụ xuất thêm các định dạng phục vụ in ấn rõ nét.

## File chính

- `tool.html`: công cụ mở bằng trình duyệt, chọn ảnh mẫu và xuất PNG A4 300DPI hoặc in/lưu PDF.
- `src/build_print_files.py`: script Python xuất PNG, JPG và PDF A4 300DPI từ ảnh gốc.
- Bản ZIP từ ChatGPT có thêm các file in sẵn: PDF A4 300DPI, PNG A4 300DPI, JPG chất lượng cao và SVG.

## Cách dùng trên GitHub Pages

Mở `tool.html`, chọn chính ảnh mẫu đã gửi, sau đó bấm tải PNG A4 300DPI hoặc in/lưu PDF.

## Cách chạy bằng Python

Đặt ảnh mẫu vào `assets/poster-original.png`, sau đó chạy:

```bash
python src/build_print_files.py
```

## Lưu ý kỹ thuật

Ảnh người, logo, icon và chữ trong mẫu đang nằm trong một file ảnh phẳng. Vì vậy cách duy nhất để giống mẫu gần như tuyệt đối là dùng chính ảnh mẫu làm nguồn. File A4 300DPI đã được nội suy và làm sắc nhẹ để in rõ hơn, nhưng không thể tạo thêm chi tiết thật nếu ảnh gốc không có.

Muốn vừa giống mẫu vừa chỉnh được từng chữ/icon như Canva hoặc Figma, cần dựng lại thủ công theo layer từ đầu hoặc có file thiết kế gốc.
