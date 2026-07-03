from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / 'assets' / 'poster-original.png'
DIST = BASE / 'dist'
DIST.mkdir(parents=True, exist_ok=True)

if not SRC.exists():
    raise FileNotFoundError('Hay dat anh mau vao: assets/poster-original.png')

img = Image.open(SRC).convert('RGB')
img.save(DIST / 'lop-hoc-so-nguyen-du-exact.png', optimize=True)
img.save(DIST / 'lop-hoc-so-nguyen-du-exact.jpg', quality=95, optimize=True, progressive=True)

a4 = img.resize((2480, 3508), Image.Resampling.LANCZOS)
a4 = a4.filter(ImageFilter.UnsharpMask(radius=1.1, percent=115, threshold=3))
a4 = ImageEnhance.Sharpness(a4).enhance(1.05)
a4.save(DIST / 'lop-hoc-so-nguyen-du-a4-300dpi.png', dpi=(300, 300), optimize=True)
a4.save(DIST / 'lop-hoc-so-nguyen-du-a4-300dpi.jpg', quality=96, dpi=(300, 300), optimize=True, progressive=True)
a4.save(DIST / 'lop-hoc-so-nguyen-du-a4-300dpi.pdf', 'PDF', resolution=300.0)

print('Da xuat file in an vao thu muc dist')
