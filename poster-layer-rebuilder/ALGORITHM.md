# Thuật toán dựng lại poster thành SVG chất lượng cao

Mục tiêu hiện tại không còn là cắt ảnh phẳng thành nhiều mảnh, mà là **dựng lại poster bằng SVG vector có thể xem trước, tải về và mở bằng Figma/Inkscape/Illustrator**.

## 1. Nguồn tài nguyên

### 1.1. Logo trường

- Dùng logo trường do người dùng cung cấp.
- Trong file SVG, logo được đặt trong group `school_logo`.
- Khi có logo SVG gốc của trường, thay trực tiếp vào group này để đạt chất lượng in tốt nhất.

### 1.2. Logo và icon Google Workspace

Nguồn tham khảo Internet:

- Google for Education: `https://edu.google.com/`
- Google Workspace: `https://workspace.google.com/`
- Google Classroom: `https://en.wikipedia.org/wiki/Google_Classroom`
- Google Drive: `https://en.wikipedia.org/wiki/Google_Drive`
- Google for Education: `https://en.wikipedia.org/wiki/Google_for_Education`

Lưu ý: logo Google và icon ứng dụng là tài sản thương hiệu của Google. Vì vậy, poster chính không hotlink file từ bên ngoài. Thay vào đó, hệ thống dựng lại icon bằng SVG vector gần giống giao diện nhận diện, giúp:

- không phụ thuộc mạng khi export;
- tránh lỗi CORS khi tải PNG/PDF;
- giữ độ nét khi phóng to;
- dễ sửa trong Figma.

## 2. Cấu trúc thiết kế

Poster SVG được chia thành các group/layer chính:

1. `decor`: chấm trang trí và mảng màu Google bên phải.
2. `header`: logo trường, tên trường, Google for Education.
3. `title`: tiêu đề chính và subtitle.
4. `hero`: banner lớp học, dựng bằng vector để giữ độ nét.
5. `section1`: tiêu đề phần 1.
6. `cards`: 4 thẻ mô tả cách học trong lớp học số.
7. `section2`: tiêu đề phần 2.
8. `apps`: hàng ứng dụng Google Workspace và Chromebook tile.
9. `benefits`: phần lợi ích cho học sinh, phụ huynh và nhà trường.
10. `device`: phần Chromebook.
11. `footer`: thông tin liên hệ chỉ gồm website và hotline.

## 3. Pipeline dựng lại bằng code

### Bước 1: Xác định hệ tọa độ

- Kích thước chuẩn: `1054 x 1493`.
- Tất cả phần tử dùng tọa độ cố định để bám sát mẫu.
- Khi cần in lớn, trình duyệt hoặc script có thể export PNG 2x/4x từ SVG.

### Bước 2: Dựng thư viện symbol SVG

Các icon được định nghĩa một lần trong `<defs>`:

- `file`: dùng cho Docs, Sheets, Slides, Forms với màu khác nhau.
- `drive`: icon Drive dạng tam giác nhiều màu.
- `gmail`: icon Gmail dạng chữ M.
- `meet`: icon Meet dạng camera.
- `classroom`: icon Classroom dạng bảng xanh.
- `laptop`: icon Chromebook.

### Bước 3: Dựng layout chính

- Header dùng logo trường, school name và Google wordmark.
- Title dùng text thật, không raster.
- Card, row, footer, divider đều là shape vector.
- Hero banner được dựng bằng vector minh họa để nét hơn ảnh raster.

### Bước 4: Preview và download

File `svg-studio/index.html` cung cấp:

- Preview trực tiếp `poster.svg`.
- Nút `Download SVG`.
- Nút `Download PNG 2x`.
- Nút `Download PNG 4x`.
- Nút `Print / Save PDF`.

Việc export PNG được thực hiện bằng Canvas trong trình duyệt từ SVG cùng origin, tránh lỗi CORS.

## 4. File đầu ra

- `svg-studio/poster.svg`: bản poster SVG chi tiết.
- `svg-studio/index.html`: giao diện preview/download.
- `svg-studio/asset-sources.json`: danh mục nguồn logo/icon tham khảo.
- `svg-studio/README.md`: hướng dẫn sử dụng.

## 5. Giới hạn kỹ thuật

- Không thể khôi phục file Figma/PSD gốc 100% từ ảnh phẳng.
- Nếu muốn giống mẫu tuyệt đối như file gốc, cần file thiết kế gốc hoặc toàn bộ logo/icon/ảnh gốc dạng vector.
- Bản hiện tại ưu tiên: **độ nét, có layer, xuất SVG/PNG/PDF thuận tiện, dễ chỉnh sửa trong Figma**.

## 6. Hướng cải tiến tiếp theo

1. Thay logo trường PNG bằng SVG gốc nếu trường cung cấp.
2. Thay hero vector bằng ảnh chụp lớp học thật chất lượng cao hoặc ảnh AI 4K được duyệt.
3. Bổ sung file `poster.fig.json` hoặc dùng plugin Figma API để tạo layer native trong Figma.
4. Tách CSS variables cho màu, font, kích thước để sửa nhanh.
5. Thêm workflow GitHub Actions tự build PNG/PDF từ SVG.
