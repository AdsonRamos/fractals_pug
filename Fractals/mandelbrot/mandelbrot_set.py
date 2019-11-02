from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, MAX_ITER

# Image size (pixels)
WIDTH = 600
HEIGHT = 400

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START), IM_START + (y / HEIGHT) * (IM_END - IM_START))
        m = mandelbrot(c)
        hue = int(255 * m / MAX_ITER)
        saturation = 91
        value = 255 if m < MAX_ITER else 96
        draw.point([x, y], (hue, saturation, value))
im.convert('RGB').save('mandelbrot.png', 'PNG')
