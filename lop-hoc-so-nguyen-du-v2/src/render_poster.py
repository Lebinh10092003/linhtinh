from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1054, 1493
S = 2
BASE_DIR = Path(__file__).resolve().parents[1]
OUT = BASE_DIR / "dist" / "lop-hoc-so-nguyen-du-v2.png"

BLUE = '#0969d8'
BLUE_D = '#064ca5'
GREEN = '#16a34a'
RED = '#e53935'
ORANGE = '#ff9f1a'
PURPLE = '#6d3bbf'
TEXT = '#263447'
LINE = '#d8e8f7'
BG = '#ffffff'
CARD = '#ffffff'

font_paths = {
    'bold': '/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf',
    'black': '/usr/share/fonts/opentype/inter/InterDisplay-Black.otf',
    'semi': '/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf',
    'reg': '/usr/share/fonts/opentype/inter/InterDisplay-Regular.otf',
}
for k, v in list(font_paths.items()):
    if not Path(v).exists():
        font_paths[k] = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if k in ['bold', 'black', 'semi'] else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

def F(size, weight='reg'):
    return ImageFont.truetype(font_paths.get(weight, font_paths['reg']), int(size * S))

def sc(v):
    return int(round(v * S))

def xybox(box):
    return tuple(sc(x) for x in box)

def rounded(draw, box, r, fill, outline=None, width=1):
    draw.rounded_rectangle(xybox(box), radius=sc(r), fill=fill, outline=outline, width=sc(width))

def rect(draw, box, fill, outline=None, width=1):
    draw.rectangle(xybox(box), fill=fill, outline=outline, width=sc(width))

def ellipse(draw, box, fill, outline=None, width=1):
    draw.ellipse(xybox(box), fill=fill, outline=outline, width=sc(width))

def line(draw, pts, fill, width=1):
    draw.line([(sc(x), sc(y)) for x, y in pts], fill=fill, width=sc(width), joint='curve')

def polygon(draw, pts, fill, outline=None):
    draw.polygon([(sc(x), sc(y)) for x, y in pts], fill=fill, outline=outline)

def txt(draw, x, y, text, font, fill=TEXT, anchor=None, align='left', spacing=4):
    draw.text((sc(x), sc(y)), text, font=font, fill=fill, anchor=anchor, align=align, spacing=sc(spacing))

def text_size(draw, text, font):
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[2] - bb[0], bb[3] - bb[1]

def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ''
    for w in words:
        test = w if not cur else cur + ' ' + w
        if text_size(draw, test, font)[0] <= sc(max_width):
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(draw, x, y, text, font, fill, max_width, line_h=None):
    lines = wrap_text(draw, text, font, max_width)
    if line_h is None:
        line_h = font.size // S + 4
    for i, line_text in enumerate(lines):
        txt(draw, x, y + i * line_h, line_text, font, fill)
    return y + len(lines) * line_h

def section_head(draw, x, y, w, num, title, color=BLUE):
    rounded(draw, (x, y, x + w, y + 34), 17, color)
    ellipse(draw, (x + 5, y + 3, x + 35, y + 33), '#ffffff')
    txt(draw, x + 20, y + 21, str(num), F(18, 'black'), color, anchor='mm')
    txt(draw, x + 48, y + 22, title, F(17, 'black'), '#ffffff', anchor='lm')

def benefit_rows(draw, x, y, w, items, color):
    for i, (title, desc) in enumerate(items):
        yy = y + i * 51
        rounded(draw, (x, yy, x + w, yy + 44), 10, '#ffffff', LINE, 1)
        ellipse(draw, (x + 12, yy + 9, x + 36, yy + 33), '#eef6ff' if color == BLUE else '#fff3d8', color, 2)
        txt(draw, x + 48, yy + 15, title, F(11.5, 'black'), color)
        txt(draw, x + 48, yy + 31, desc, F(9.3, 'reg'), TEXT)

def render():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    im = Image.new('RGB', (W * S, H * S), BG)
    d = ImageDraw.Draw(im)

    ellipse(d, (960, 160, 1160, 360), '#eaf7ef')
    ellipse(d, (990, 170, 1200, 390), '#fff0d2')
    ellipse(d, (1010, 140, 1210, 330), '#ffe6e4')
    for i in range(7):
        for j in range(9):
            ellipse(d, (20 + i * 16, 185 + j * 16, 25 + i * 16, 190 + j * 16), '#d8eafe')

    ellipse(d, (24, 28, 101, 105), '#f5fbff', BLUE, 3)
    polygon(d, [(50, 52), (63, 42), (76, 52), (76, 82), (63, 92), (50, 82)], '#ffffff', BLUE)
    line(d, [(63, 42), (63, 92)], BLUE, 2)
    line(d, [(50, 52), (63, 62), (76, 52)], BLUE, 2)
    txt(d, 126, 48, 'TRƯỜNG TRUNG HỌC CƠ SỞ', F(13, 'bold'), BLUE_D)
    txt(d, 126, 76, 'NGUYỄN DU', F(33, 'black'), BLUE_D)

    x0, y0 = 735, 42
    colors = ['#4285F4', '#DB4437', '#F4B400', '#4285F4', '#0F9D58', '#DB4437']
    for ch, c in zip('Google', colors):
        txt(d, x0, y0, ch, F(25, 'bold'), c)
        x0 += text_size(d, ch, F(25, 'bold'))[0] / S + 1
    txt(d, x0 + 4, y0 + 2, 'for Education', F(24, 'reg'), '#3a3a3a')

    cx = 527
    txt(d, cx, 148, 'LỚP HỌC SỐ:', F(42, 'black'), BLUE, anchor='mm')
    txt(d, cx, 203, 'CON HỌC GÌ,', F(42, 'black'), RED, anchor='mm')
    txt(d, cx, 258, 'HỌC THẾ NÀO, HỌC BẰNG GÌ?', F(39, 'black'), GREEN, anchor='mm')
    txt(d, cx, 309, 'Với Google Workspace for Education, học sinh được học tập', F(16, 'semi'), BLUE_D, anchor='mm')
    txt(d, cx, 330, 'trên một hệ sinh thái hiện đại giúp tăng hiệu quả, kết nối và kỹ năng số.', F(16, 'semi'), BLUE_D, anchor='mm')

    for x, c in zip([540, 600, 660, 720, 780], [BLUE, GREEN, ORANGE, PURPLE, RED]):
        rounded(d, (x, 345, x + 34, 385), 5, c)
        rect(d, (x + 7, 355, x + 27, 359), '#ffffff')
        rect(d, (x + 7, 364, x + 24, 368), '#ffffff')

    rounded(d, (25, 360, 1029, 566), 22, '#f9fcff', LINE, 1)
    rounded(d, (30, 365, 1024, 560), 18, '#fffaf0')
    rect(d, (35, 368, 350, 545), '#f7fbff')
    rect(d, (715, 370, 1018, 545), '#fffaf0')
    for x in [65, 120, 175, 230]:
        rect(d, (x, 385, x + 38, 462), '#e6f2ff', '#d5e8fa')
    rect(d, (805, 405, 980, 415), '#d2b48c')
    for i, c in enumerate(['#f66', '#6cc', '#fdc', '#9c6', '#6af']):
        rect(d, (820 + i * 27, 370, 838 + i * 27, 405), c)
    ellipse(d, (930, 385, 985, 440), '#cce9ff', '#6aa7d8', 2)
    rect(d, (952, 440, 963, 465), '#d2b48c')
    rect(d, (925, 465, 990, 473), '#d2b48c')
    rounded(d, (25, 505, 1029, 590), 18, '#f2c88f')
    rect(d, (25, 555, 1029, 590), '#eab27a')

    ellipse(d, (492, 380, 548, 436), '#f3bf96')
    ellipse(d, (484, 371, 556, 430), '#5b3927')
    ellipse(d, (498, 388, 542, 436), '#f3bf96')
    polygon(d, [(470, 435), (570, 435), (615, 535), (430, 535)], '#fff0cf', '#d6bd82')
    line(d, [(510, 458), (475, 505), (445, 540)], '#f3bf96', 9)
    line(d, [(550, 458), (585, 505), (615, 540)], '#f3bf96', 9)

    students = [(130, 445, '#1f2937'), (315, 450, '#2e2a52'), (690, 450, '#2b2b2b'), (865, 452, '#171717')]
    for x, y, hair in students:
        ellipse(d, (x - 34, y - 66, x + 34, y + 2), hair)
        ellipse(d, (x - 28, y - 52, x + 28, y + 4), '#f1c29a')
        rounded(d, (x - 48, y + 3, x + 48, y + 55), 15, '#ffffff', '#d7e3ee')
        polygon(d, [(x - 25, y + 3), (x, y + 22), (x + 25, y + 3)], '#f2f7fd')
        rounded(d, (x - 62, y + 42, x + 62, y + 107), 5, '#7c8fa3')
        rounded(d, (x - 54, y + 50, x + 54, y + 95), 3, '#9fb3c8')
        rect(d, (x - 75, y + 106, x + 75, y + 114), '#5f7285')

    section_head(d, 25, 595, 420, 1, 'Con học thế nào trong lớp học số?', BLUE)
    cards = [
        ('1', 'Nhận bài và hướng dẫn\ntrên Google Classroom', 'Giáo viên giao bài, chia sẻ học liệu và hướng dẫn rõ ràng.', GREEN, 'C'),
        ('2', 'Học tập, soạn bài,\ntrình bày trên Docs, Sheets, Slides', 'Soạn thảo, tính toán, thiết kế slide và làm việc mọi lúc, mọi nơi.', ORANGE, 'D'),
        ('3', 'Làm bài tập, bài kiểm tra\nvà khảo sát trên Google Forms', 'Nộp bài, làm bài kiểm tra và khảo sát trực tuyến dễ dàng.', PURPLE, 'F'),
        ('4', 'Trao đổi, họp lớp, nhận phản hồi\nqua Gmail, Meet và Drive', 'Liên lạc nhanh, học trực tuyến và lưu trữ an toàn.', RED, 'M'),
    ]
    card_w, gap, y = 235, 17, 640
    for i, (num, title, desc, col, letter) in enumerate(cards):
        x = 25 + i * (card_w + gap)
        rounded(d, (x, y, x + card_w, y + 190), 16, CARD, LINE, 1)
        ellipse(d, (x + 12, y + 15, x + 42, y + 45), col)
        txt(d, x + 27, y + 31, num, F(17, 'black'), '#fff', anchor='mm')
        rounded(d, (x + 83, y + 17, x + 128, y + 62), 8, col)
        txt(d, x + 105.5, y + 41, letter, F(23, 'black'), '#fff', anchor='mm')
        yy = y + 80
        for tl in title.split('\n'):
            txt(d, x + card_w / 2, yy, tl, F(13, 'black'), col, anchor='mm')
            yy += 18
        draw_wrapped(d, x + 22, y + 127, desc, F(11.2, 'reg'), TEXT, card_w - 44, 15)

    section_head(d, 25, 850, 540, 2, 'Những ứng dụng học sinh sẽ dùng thường xuyên', GREEN)
    apps = [
        ('Classroom', GREEN, 'Quản lý lớp học, nhận bài và theo dõi tiến độ'),
        ('Docs', BLUE, 'Soạn thảo văn bản, viết báo cáo, làm việc nhóm'),
        ('Slides', ORANGE, 'Thiết kế bài trình bày, thuyết trình sáng tạo'),
        ('Sheets', GREEN, 'Tính toán, phân tích dữ liệu, lập biểu đồ'),
        ('Forms', PURPLE, 'Làm bài tập, kiểm tra và khảo sát trực tuyến'),
        ('Drive', GREEN, 'Lưu trữ, chia sẻ và đồng bộ tài liệu'),
        ('Gmail', RED, 'Email an toàn, nhận thông báo và trao đổi'),
        ('Meet', GREEN, 'Họp trực tuyến, học online, tương tác dễ dàng'),
        ('Chromebook', BLUE, 'Thiết bị học tập lý tưởng cho môi trường số'),
    ]
    x, y, w, h, gap = 25, 895, 104, 116, 8
    for i, (name, col, desc) in enumerate(apps):
        xx = x + i * (w + gap)
        rounded(d, (xx, y, xx + w, y + h), 14, '#ffffff', LINE, 1)
        rounded(d, (xx + 33, y + 13, xx + 70, y + 49), 7, col)
        txt(d, xx + 52, y + 34, name[0], F(18, 'black'), '#fff', anchor='mm')
        txt(d, xx + w / 2, y + 65, name, F(11.5, 'black'), col, anchor='mm')
        draw_wrapped(d, xx + 9, y + 82, desc, F(7.7, 'reg'), TEXT, w - 18, 10)

    section_head(d, 25, 1040, 480, 3, 'Lợi ích đối với học sinh', BLUE)
    section_head(d, 535, 1040, 494, 4, 'Lợi ích đối với phụ huynh và nhà trường', ORANGE)
    benefits_left = [
        ('Dễ tiếp cận học liệu', 'Truy cập tài liệu mọi lúc, mọi nơi trên mọi thiết bị.'),
        ('Rèn kỹ năng số', 'Làm quen và thành thạo các công cụ số cần thiết.'),
        ('Hợp tác hiệu quả', 'Làm việc nhóm dễ dàng, chia sẻ và hỗ trợ lẫn nhau.'),
        ('Sáng tạo và thuyết trình tốt hơn', 'Tạo sản phẩm học tập sinh động, trình bày ấn tượng.'),
        ('Tự học tốt hơn', 'Chủ động học tập, quản lý thời gian và theo dõi tiến bộ.'),
    ]
    benefits_right = [
        ('Dễ phối hợp cùng giáo viên', 'Trao đổi nhanh, nắm bắt thông tin học tập kịp thời.'),
        ('Nắm bắt hành trình học tập của con', 'Theo dõi tiến độ, kết quả và hoạt động học tập.'),
        ('Dữ liệu học tập rõ ràng', 'Báo cáo minh bạch, hỗ trợ con học tập tốt hơn.'),
        ('Môi trường học tập an toàn', 'Hệ thống bảo mật, kiểm soát nội dung và quyền truy cập.'),
        ('Quản lý tập trung, hiệu quả', 'Tiết kiệm thời gian, tối ưu vận hành cho nhà trường.'),
    ]
    benefit_rows(d, 25, 1085, 480, benefits_left, BLUE)
    benefit_rows(d, 535, 1085, 494, benefits_right, ORANGE)

    section_head(d, 25, 1328, 260, 5, 'Con học bằng gì?', BLUE)
    rounded(d, (25, 1370, 1029, 1432), 20, '#f8fcff', '#b9dcfb', 1)
    rounded(d, (65, 1382, 170, 1420), 6, '#1f2937')
    rect(d, (72, 1388, 163, 1412), '#bae6fd')
    rect(d, (54, 1420, 181, 1427), '#64748b')
    txt(d, 235, 1395, 'Chromebook', F(23, 'black'), BLUE_D)
    txt(d, 235, 1418, 'Thiết bị học tập được thiết kế cho môi trường giáo dục hiện đại.', F(10, 'reg'), TEXT)
    features = [
        ('Khởi động nhanh', 'Bật máy và vào lớp chỉ trong vài giây.'),
        ('Dễ dùng', 'Giao diện đơn giản, phù hợp mọi lứa tuổi.'),
        ('Pin lâu', 'Sử dụng cả ngày dài không lo gián đoạn.'),
        ('Bảo mật tốt', 'Tự động cập nhật, bảo vệ dữ liệu và thiết bị.'),
    ]
    fx = 475
    for i, (a, b) in enumerate(features):
        xx = fx + i * 132
        ellipse(d, (xx, 1384, xx + 32, 1416), '#eef6ff', BLUE, 2)
        txt(d, xx + 16, 1400, str(i + 1), F(13, 'black'), BLUE, anchor='mm')
        txt(d, xx + 40, 1394, a, F(9.8, 'black'), BLUE if i < 3 else RED)
        draw_wrapped(d, xx + 40, 1409, b, F(7.8, 'reg'), TEXT, 86, 9)

    rect(d, (0, 1438, 1054, 1493), BLUE)
    ellipse(d, (28, 1452, 65, 1489), '#0d7bf2')
    txt(d, 85, 1458, 'LIÊN HỆ NHÀ TRƯỜNG', F(15, 'black'), '#fff')
    txt(d, 85, 1478, 'ĐỂ TÌM HIỂU THÊM', F(15, 'black'), '#fff')
    rounded(d, (350, 1450, 412, 1487), 8, '#ffffff')
    txt(d, 381, 1467, 'QR', F(12, 'black'), BLUE, anchor='mm')
    txt(d, 381, 1482, 'CODE', F(9, 'black'), BLUE, anchor='mm')
    footer = [('Hotline', '0123 456 789'), ('Website', 'www.truongnguyendu.vn'), ('Email', 'thcs@truongnguyendu.vn'), ('Địa chỉ', 'Hà Nội')]
    fx = 450
    for label, val in footer:
        txt(d, fx, 1458, label, F(8.5, 'semi'), '#dceeff')
        txt(d, fx, 1475, val, F(8.2, 'reg'), '#ffffff')
        fx += 150

    im = im.resize((W, H), Image.Resampling.LANCZOS)
    im.save(OUT)
    print(f'Da xuat anh: {OUT}')

if __name__ == '__main__':
    render()
