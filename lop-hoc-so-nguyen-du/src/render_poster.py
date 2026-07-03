from pathlib import Path
import cairosvg

BASE_DIR = Path(__file__).resolve().parents[1]
svg_path = BASE_DIR / "dist" / "lop-hoc-so-nguyen-du.svg"
png_path = BASE_DIR / "dist" / "lop-hoc-so-nguyen-du.png"

if not svg_path.exists():
    raise FileNotFoundError(f"Không tìm thấy file SVG: {svg_path}")

cairosvg.svg2png(
    url=str(svg_path),
    write_to=str(png_path),
    output_width=1240,
    output_height=1940,
)

print(f"Đã xuất PNG: {png_path}")
