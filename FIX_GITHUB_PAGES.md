# Sửa lỗi GitHub Pages deployment failed

## Đã thêm

- `.github/workflows/pages.yml`: workflow deploy GitHub Pages chuẩn bằng GitHub Actions.
- `index.html`: trang chủ để tránh lỗi repo không có trang index.
- `.nojekyll`: tránh GitHub Pages xử lý Jekyll không cần thiết.

## Cần kiểm tra trên GitHub

Vào Settings > Pages:

- Source: GitHub Actions

Sau đó vào Actions > Pages > Run workflow hoặc rerun workflow mới nhất.

## Nếu trang đúng mẫu bị thiếu ảnh

Cần upload thêm file ảnh đúng mẫu vào đường dẫn:

`lop-hoc-so-nguyen-du-exact/dist/lop-hoc-so-nguyen-du-exact.png`

Có thể lấy file ảnh trong ZIP ChatGPT đã xuất, sau đó push lên repo bằng lệnh:

```bash
git add lop-hoc-so-nguyen-du-exact/dist/lop-hoc-so-nguyen-du-exact.png
git commit -m "Add exact poster PNG"
git push
```
