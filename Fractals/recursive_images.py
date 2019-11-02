from builtins import dict

from PIL import ImageDraw, Image

# image size
scale = 4
WIDTH = 320 * scale
HEIGHT = 240 * scale

d = 500

im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

xP = WIDTH/2 - d / 2
yP = HEIGHT / 2 - d / 2


def circles(x, y, diameter):
    draw.ellipse((x, y, x + diameter, y + diameter), outline=(244, 172, 183))
    if diameter > 25:
        circles(x - 0.3*diameter, y + diameter / 10, diameter * 0.8)
        circles(x + 0.5*diameter, y + diameter / 10, diameter * 0.8)


circles(xP, yP, d)

im.convert('RGB').save('circles.png', 'PNG')
