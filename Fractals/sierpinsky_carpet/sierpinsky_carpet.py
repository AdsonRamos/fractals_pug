from PIL import ImageDraw, Image

# image size
WIDTH = 1080
HEIGHT = 1080
l = 300

im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)


def carpet(x, y, length):
    draw.rectangle((x - length / 2, y - length / 2, x - length / 2 + length, y - length / 2 + length),
                   fill=(255, 255, 255))
    if length > 20:
        carpet(x - length, y - length, length / 3)
        carpet(x + length, y - length, length / 3)
        carpet(x - length, y + length, length / 3)
        carpet(x + length, y + length, length / 3)
        carpet(x, y - length, length / 3)
        carpet(x, y + length, length / 3)
        carpet(x - length, y, length / 3)
        carpet(x + length, y, length / 3)


carpet(WIDTH / 2, HEIGHT / 2, l)

im.convert('RGB').save('sierpinsky_carpet.png', 'PNG')
