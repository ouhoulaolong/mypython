import turtle
import math

# ========== 初始化设置 ==========
screen = turtle.Screen()
screen.bgcolor("#87CEEB")  # 天蓝色背景
screen.title("精致的卡皮巴拉")
screen.setup(900, 700)

pen = turtle.Turtle()
pen.speed(0)  # 最快速度
pen.hideturtle()

# ========== 颜色定义 ==========
COLORS = {
    "body_dark": "#8B7355",  # 深棕褐色身体底色
    "body_light": "#A1887F",  # 浅棕褐色高光
    "fur_dark": "#6D4C41",  # 深色毛发
    "fur_mid": "#8D6E63",  # 中间色毛发
    "fur_light": "#BCAAA4",  # 浅色毛发
    "eye_white": "#FFFFFF",  # 眼白
    "eye_pupil": "#2C3E50",  # 深蓝黑瞳孔
    "eye_shine": "#ECF0F1",  # 眼睛高光
    "nose": "#5D4037",  # 鼻子深色
    "nose_highlight": "#8B7355",  # 鼻子高光
    "inner_ear": "#D7CCC8",  # 耳朵内侧
    "whisker": "#757575",  # 胡须颜色
    "mouth": "#795548",  # 嘴巴颜色
    "claw": "#5D4037",  # 爪子颜色
}


# ========== 高级绘图函数 ==========
def draw_ellipse(t, x, y, width, height, color, angle=0, outline=False):
    """绘制带旋转的椭圆"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    if color:
        t.color(color)
        t.begin_fill()

    rx = width / 2
    ry = height / 2

    # 更精确的椭圆绘制
    t.penup()
    for i in range(361):
        rad = math.radians(i)
        px = rx * math.cos(rad)
        py = ry * math.sin(rad)

        # 旋转
        px_rot = px * math.cos(math.radians(angle)) - py * math.sin(math.radians(angle))
        py_rot = px * math.sin(math.radians(angle)) + py * math.cos(math.radians(angle))

        t.goto(x + px_rot, y + py_rot)
        if i == 0:
            t.pendown()

    if color:
        t.end_fill()

    if outline:
        t.penup()
        t.goto(x + rx * math.cos(math.radians(angle)),
               y + rx * math.sin(math.radians(angle)))
        t.pendown()
        t.color("#5D4037")
        t.width(1.5)
        t.circle(rx, 360, steps=100)


def draw_fur_texture(t, x, y, radius, color1, color2, count=30):
    """绘制毛发纹理效果"""
    t.penup()
    for _ in range(count):
        angle = math.radians(random.uniform(0, 360))
        dist = random.uniform(0, radius * 0.8)
        fx = x + math.cos(angle) * dist
        fy = y + math.sin(angle) * dist
        length = random.uniform(3, 8)

        t.goto(fx, fy)
        t.setheading(math.degrees(angle) + 90)
        t.pendown()
        t.color(color1 if random.random() > 0.5 else color2)
        t.width(random.uniform(0.5, 1.2))
        t.forward(length)
        t.penup()


def draw_gradient_circle(t, x, y, radius, color1, color2, steps=10):
    """绘制渐变圆形"""
    for i in range(steps, 0, -1):
        r = radius * i / steps
        # 计算混合颜色
        ratio = i / steps
        r_color = color1[0] * ratio + color2[0] * (1 - ratio)
        g_color = color1[1] * ratio + color2[1] * (1 - ratio)
        b_color = color1[2] * ratio + color2[2] * (1 - ratio)

        t.penup()
        t.goto(x, y - r)
        t.pendown()
        t.color((r_color, g_color, b_color))
        t.begin_fill()
        t.circle(r)
        t.end_fill()


# ========== 身体部分绘制函数 ==========
def draw_body():
    """绘制身体主体"""
    # 身体主体（带轻微渐变）
    pen.color(COLORS["body_dark"])
    pen.begin_fill()
    draw_ellipse(pen, -100, -60, 220, 130, COLORS["body_dark"], angle=5)
    pen.end_fill()

    # 身体高光区域
    pen.color(COLORS["body_light"])
    pen.begin_fill()
    draw_ellipse(pen, -80, -40, 180, 100, COLORS["body_light"], angle=5)
    pen.end_fill()


def draw_head():
    """绘制头部"""
    # 头部基础形状
    pen.color(COLORS["body_dark"])
    pen.begin_fill()
    draw_ellipse(pen, 80, 30, 120, 90, COLORS["body_dark"], angle=-10)
    pen.end_fill()

    # 脸颊高光
    pen.color(COLORS["body_light"])
    pen.begin_fill()
    draw_ellipse(pen, 100, 20, 70, 60, COLORS["body_light"], angle=-10)
    pen.end_fill()


def draw_eyes():
    """绘制眼睛（更精致）"""
    # 左眼
    pen.penup()
    pen.goto(120, 70)
    pen.pendown()
    pen.color(COLORS["eye_white"])
    pen.begin_fill()
    pen.circle(12)
    pen.end_fill()

    # 左眼虹膜
    pen.penup()
    pen.goto(124, 74)
    pen.pendown()
    pen.color("#3498DB")  # 蓝色虹膜
    pen.begin_fill()
    pen.circle(8)
    pen.end_fill()

    # 左眼瞳孔
    pen.penup()
    pen.goto(126, 76)
    pen.pendown()
    pen.color(COLORS["eye_pupil"])
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

    # 左眼高光
    pen.penup()
    pen.goto(128, 80)
    pen.pendown()
    pen.color(COLORS["eye_shine"])
    pen.begin_fill()
    pen.circle(2)
    pen.end_fill()

    # 右眼（类似左眼）
    pen.penup()
    pen.goto(70, 80)
    pen.pendown()
    pen.color(COLORS["eye_white"])
    pen.begin_fill()
    pen.circle(11)
    pen.end_fill()

    pen.penup()
    pen.goto(73, 83)
    pen.pendown()
    pen.color("#3498DB")
    pen.begin_fill()
    pen.circle(7)
    pen.end_fill()

    pen.penup()
    pen.goto(75, 85)
    pen.pendown()
    pen.color(COLORS["eye_pupil"])
    pen.begin_fill()
    pen.circle(4)
    pen.end_fill()

    pen.penup()
    pen.goto(77, 88)
    pen.pendown()
    pen.color(COLORS["eye_shine"])
    pen.begin_fill()
    pen.circle(1.5)
    pen.end_fill()


def draw_nose():
    """绘制鼻子"""
    # 鼻子主体
    pen.penup()
    pen.goto(110, 40)
    pen.pendown()
    pen.color(COLORS["nose"])
    pen.begin_fill()
    draw_ellipse(pen, 110, 40, 30, 20, COLORS["nose"], angle=0)
    pen.end_fill()

    # 鼻子高光
    pen.penup()
    pen.goto(115, 45)
    pen.pendown()
    pen.color(COLORS["nose_highlight"])
    pen.begin_fill()
    pen.circle(6)
    pen.end_fill()

    # 鼻孔
    pen.penup()
    pen.goto(105, 42)
    pen.pendown()
    pen.color("#4A342E")
    pen.begin_fill()
    pen.circle(3)
    pen.end_fill()

    pen.penup()
    pen.goto(115, 42)
    pen.pendown()
    pen.begin_fill()
    pen.circle(3)
    pen.end_fill()


def draw_ears():
    """绘制耳朵"""
    # 左耳
    pen.penup()
    pen.goto(140, 90)
    pen.pendown()
    pen.color(COLORS["body_dark"])
    pen.begin_fill()
    draw_ellipse(pen, 140, 90, 25, 20, COLORS["body_dark"], angle=30)
    pen.end_fill()

    # 左耳内侧
    pen.penup()
    pen.goto(138, 92)
    pen.pendown()
    pen.color(COLORS["inner_ear"])
    pen.begin_fill()
    draw_ellipse(pen, 138, 92, 18, 15, COLORS["inner_ear"], angle=30)
    pen.end_fill()

    # 右耳
    pen.penup()
    pen.goto(50, 100)
    pen.pendown()
    pen.color(COLORS["body_dark"])
    pen.begin_fill()
    draw_ellipse(pen, 50, 100, 28, 22, COLORS["body_dark"], angle=-20)
    pen.end_fill()

    # 右耳内侧
    pen.penup()
    pen.goto(48, 102)
    pen.pendown()
    pen.color(COLORS["inner_ear"])
    pen.begin_fill()
    draw_ellipse(pen, 48, 102, 20, 16, COLORS["inner_ear"], angle=-20)
    pen.end_fill()


def draw_mouth():
    """绘制嘴巴"""
    # 上唇
    pen.penup()
    pen.goto(90, 30)
    pen.pendown()
    pen.color(COLORS["mouth"])
    pen.width(2)
    pen.setheading(-20)
    pen.circle(25, 40)

    # 下唇
    pen.penup()
    pen.goto(90, 30)
    pen.pendown()
    pen.setheading(-20)
    pen.right(180)
    pen.circle(25, -30)

    # 嘴巴线条
    pen.penup()
    pen.goto(100, 20)
    pen.pendown()
    pen.setheading(-10)
    pen.forward(25)


def draw_whiskers():
    """绘制胡须"""
    pen.color(COLORS["whisker"])
    pen.width(1.2)

    # 左侧胡须
    positions = [(100, 35), (102, 30), (104, 25)]
    for x, y in positions:
        for angle in [160, 180, 200]:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.setheading(angle)
            pen.forward(25)

    # 右侧胡须
    positions = [(85, 35), (83, 30), (81, 25)]
    for x, y in positions:
        for angle in [0, 20, 340]:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.setheading(angle)
            pen.forward(25)


def draw_legs():
    """绘制腿部"""
    leg_positions = [
        (-60, -60, 25, 40, 20),  # 左前腿
        (-10, -65, 25, 45, 15),  # 右前腿
        (40, -70, 25, 50, 10),  # 左后腿
        (90, -75, 25, 55, 5)  # 右后腿
    ]

    for x, y, width, height, angle in leg_positions:
        # 腿部主体
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color(COLORS["body_dark"])
        pen.begin_fill()
        draw_ellipse(pen, x, y, width, height, COLORS["body_dark"], angle=angle)
        pen.end_fill()

        # 脚掌
        pen.penup()
        pen.goto(x, y - height / 2 - 5)
        pen.pendown()
        pen.color(COLORS["fur_dark"])
        pen.begin_fill()
        pen.circle(width / 2 - 3)
        pen.end_fill()

        # 爪子
        pen.color(COLORS["claw"])
        pen.width(1)
        for claw_x in [x - 4, x, x + 4]:
            pen.penup()
            pen.goto(claw_x, y - height / 2 - 8)
            pen.pendown()
            pen.setheading(-90)
            pen.forward(6)


def draw_tail():
    """绘制尾巴"""
    pen.penup()
    pen.goto(-120, -30)
    pen.pendown()
    pen.color(COLORS["body_dark"])
    pen.width(8)
    pen.setheading(210)

    # 弯曲的尾巴
    for angle, length in [(200, 15), (190, 10), (180, 8)]:
        pen.setheading(angle)
        pen.forward(length)


def draw_fur_details():
    """绘制毛发细节"""
    # 身体毛发纹理
    import random

    # 在身体和头部添加随机毛发
    for _ in range(80):
        angle = random.uniform(0, 360)
        dist = random.uniform(0, 100)
        fx = random.uniform(-80, 100)
        fy = random.uniform(-40, 60)
        length = random.uniform(5, 12)

        pen.penup()
        pen.goto(fx, fy)
        pen.setheading(angle)
        pen.pendown()

        # 随机选择毛发颜色
        fur_colors = [COLORS["fur_dark"], COLORS["fur_mid"], COLORS["fur_light"]]
        pen.color(random.choice(fur_colors))
        pen.width(random.uniform(0.3, 0.8))
        pen.forward(length)
        pen.penup()


def draw_shadows():
    """绘制阴影效果"""
    # 身体阴影
    pen.penup()
    pen.goto(-50, -80)
    pen.pendown()
    pen.color("#000000")
    pen.setalpha(0.1)  # 透明度

    pen.begin_fill()
    draw_ellipse(pen, -50, -80, 180, 50, "#000000", angle=5)
    pen.end_fill()


# ========== 主绘制函数 ==========
def draw_detailed_capybara():
    print("正在绘制精致版卡皮巴拉...")

    # 按从后到前的顺序绘制
    draw_body()
    draw_head()
    draw_ears()
    draw_legs()
    draw_tail()
    draw_eyes()
    draw_nose()
    draw_mouth()
    draw_whiskers()
    draw_fur_details()

    # 添加文字
    pen.penup()
    pen.goto(0, -150)
    pen.color("#2C3E50")
    pen.write("Capybara - 水豚", align="center", font=("Arial", 20, "bold italic"))

    pen.penup()
    pen.goto(0, -180)
    pen.color("#7F8C8D")
    pen.write("世界最大的啮齿动物", align="center", font=("Microsoft YaHei", 14))


# ========== 执行绘制 ==========
import random  # 用于毛发纹理

draw_detailed_capybara()

# 完成提示
pen.penup()
pen.goto(0, -220)
pen.color("#27AE60")
pen.write("绘制完成！", align="center", font=("Arial", 16, "bold"))

print("精致卡皮巴拉绘制完成！")
screen.mainloop()