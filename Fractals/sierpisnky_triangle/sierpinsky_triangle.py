from PIL import Image, ImageDraw
import math

# image size
WIDTH = 1080
HEIGHT = 1080

im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)


def dist(x0, y0, x1, y1):
    return math.sqrt(pow(x0 - x1, 2) + pow(y0 - y1, 2))


for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        draw.point([x, y], (x % 255, (x * y) % 255, 22))


def equilateral_triangle(x, y, l):
    x0 = x
    y0 = y
    x1 = x0 + l
    y1 = y0

    draw.line((x0, y0, x1, y1), fill=(244, 172, 183))
    draw.line((x1, y1, x0 + l / 2, y0 + l * math.sin(math.pi / 3)), fill=(244, 172, 183))
    draw.line((x0 + l / 2, y0 + l * math.sin(math.pi / 3), x0, y0), fill=(244, 172, 183))


def sierpinsky(x, y, l):
    equilateral_triangle(x, y, l)
    if l > 1:
        sierpinsky(x - l / 4, y + 0.5 * l * math.sin(math.pi / 3), l / 2)
        sierpinsky(x + l / 4, y - 0.5 * l * math.sin(math.pi / 3), l / 2)
        sierpinsky(x + 3 * l / 4, y + 0.5 * l * math.sin(math.pi / 3), l / 2)


length = 500
sierpinsky(WIDTH / 2 - length / 2, HEIGHT / 2, length)
im.convert('RGB').save("triangle/sierpinsky.png", 'PNG')


