# SVG Studio - Nguyễn Du Flyer

Thư mục này có 2 chế độ dựng poster.

## Bản offline

- `index.html`: preview poster tự chứa, có nút tải SVG, PNG 2x, PNG 4x và in/lưu PDF.
- `poster.svg`: poster SVG dựng lại theo layout mẫu, có group/layer rõ ràng để mở bằng Figma/Inkscape/Illustrator.

## Bản dùng icon từ Internet

- `internet-assets.html`: dùng icon ứng dụng qua Wikimedia Commons Special:FilePath.
- Có nút upload logo trường và ảnh banner để nhúng trực tiếp vào SVG.
- Phù hợp khi cần icon giống chuẩn hơn thay vì icon tự vẽ.

## Nút tải

- `Download SVG`: tải file vector để sửa trong Figma.
- `Download PNG 2x`: xuất ảnh nét hơn để xem nhanh.
- `Download PNG 4x`: xuất ảnh lớn hơn để in/test chất lượng.
- `Print / Save PDF`: dùng trình duyệt lưu PDF.

## Ghi chú

- Bản `poster.svg` ưu tiên chạy offline, không phụ thuộc mạng.
- Bản `internet-assets.html` ưu tiên icon chuẩn hơn, nhưng phụ thuộc mạng. Khi xuất PNG nếu trình duyệt chặn ảnh ngoài, hãy dùng Download SVG hoặc upload logo/banner cục bộ trước khi xuất.
