# Thuật toán dựng lại poster thành layer

Pipeline đầy đủ trong bản ZIP gồm các bước:

1. Nhận ảnh đầu vào PNG/JPG.
2. Chuẩn hóa kích thước ảnh theo mẫu gốc.
3. Dùng blueprint để tách các vùng bố cục chính: logo, Google logo, tiêu đề, ảnh hero, từng card, app row, benefit block, device block, footer.
4. Xuất từng vùng thành layer ảnh riêng trong thư mục `layers/`.
5. Sinh SVG có group ID cho từng layer để import vào Figma/Inkscape.
6. Chạy OCR tiếng Việt + tiếng Anh để tạo lớp chữ có thể chỉnh sửa trong SVG riêng.
7. Dò vùng màu bằng HSV threshold để lấy thêm metadata layout tự động.
8. Xuất bản in: PNG/JPG/PDF A4 300DPI.
9. Xuất PSD nhiều layer bằng ImageMagick nếu máy có hỗ trợ.

Giới hạn: ảnh phẳng không chứa font gốc, ảnh gốc chưa crop, vector icon hoặc layer Photoshop/Figma ban đầu. Vì vậy muốn giống mẫu tuyệt đối về hiển thị thì phải giữ crop/raster từ ảnh gốc; muốn sửa chữ/icon hoàn toàn thì cần dựng lại thủ công dựa trên layer + OCR.
