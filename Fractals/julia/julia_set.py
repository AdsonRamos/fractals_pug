import numpy
from PIL import Image, ImageDraw
from julia import julia, MAX_ITER
from collections import defaultdict
from math import floor, ceil


def linear_interpolation(color1, color2, t):
    return color1 * (1 - t) + color2 * t


# Image size (pixels)
WIDTH = 640
HEIGHT = 640

# Plot window
RE_START = -1
RE_END = 1
IM_START = -1.2
IM_END = 1.2

# c constant used to compute the julia set
c1 = complex(0.285, 0.01)
# Other interesting values:
c2 = complex(-0.7269, 0.1889)
c3 = complex(-0.8, 0.156)


# c = complex(-0.4, 0.6)

def draw_set(complex_number, name_file):
    histogram = defaultdict(lambda: 0)
    values = {}
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            z0 = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                         IM_START + (y / HEIGHT) * (IM_END - IM_START))
            # Compute the number of iterations
            m = julia(complex_number, z0)

            values[(x, y)] = m
            if m < MAX_ITER:
                histogram[floor(m)] += 1

    total = sum(histogram.values())
    hues = []
    h = 0
    for i in range(MAX_ITER):
        h += histogram[i] / total
        hues.append(h)
    hues.append(h)

    im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            m = values[(x, y)]
            hue = 255 - int(255 * linear_interpolation(hues[floor(m)], hues[ceil(m)], m % 1))
            saturation = 255
            value = 255 if m < MAX_ITER else 43
            draw.point([x, y], (hue, saturation, value))
    im.convert('RGB').save(name_file, 'PNG')


for i in numpy.arange(0.01, 2.01, 0.01):
    c = complex(2.0 - i, -2.0 + i)
    name_file = "res/julia" + str(int(round(100 * i))) + ".png"
    draw_set(c, name_file)
