from PIL import Image
from random import randint
import tkinter as tk
from tkinter import filedialog

# https://pillow.readthedocs.io/en/3.0.x/reference/Image.html


def load_image(address):
    to_clone = Image.open(address)
    result = Image.new("RGB", (to_clone.width, to_clone.height))
    for x in range(result.width):
        for y in range(result.height):
            color = to_clone.getpixel((x,y))
            result.putpixel((x,y), color)

    return result


my_picture = Image.new("RGB", (256, 256))
for x in range(256):
    for y in range(256):
        color = (x, y, 100)
        pos = (x, y)
        my_picture.putpixel(pos, color)
#my_picture.show()


with_noise = Image.new("RGB", (256, 256))
for x in range(256):
    for y in range(256):
        color = my_picture.getpixel((x, y))
        #noisy_color = ((color[0]+randint(0, 256))//2, (color[1]+randint(0, 256))//2, (color[2]+randint(0, 256))//2)
        rand = 10
        noisy_color = (color[0]+randint(-rand, rand), color[1]+randint(-rand, rand), color[2]+randint(-rand, rand))
        with_noise.putpixel((x, y), noisy_color)
#with_noise.show()
#with_noise.save("noisy_gradient.png")


root = tk.Tk()
root.withdraw()

def tuple_multiplier(tup, multiplier):
    return tuple([multiplier*i for i in tup])

def filter_pixel(image, center_x, center_y):
    if center_x in [0, image.width-1] or center_y in [0, image.height-1]:
        return (0, 0, 0)

    filter = [[-0.25, 0, 0.25],
              [0, 0, 0],
              [0.25, 0, -0.25]]
    total = [0, 0, 0]
    for x in [-1, 0, 1]:
        for y in [-1,0,1]:
            pixel = image.getpixel((center_x+x, center_y+y))
            change = filter[1+y][1+x]
            pixel = tuple_multiplier(pixel, change)
            total[0] += pixel[0]
            total[1] += pixel[1]
            total[2] += pixel[2]
    return tuple([int(i) for i in total])

file_path = filedialog.askopenfilename()
loaded = load_image(file_path)
to_modify = load_image(file_path)
for x in range(loaded.width):
    for y in range(loaded.height):
        color = filter_pixel(loaded, x, y)
        to_modify.putpixel((x, y), color)
to_modify.show()