from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Used to create file-prompts
root = tk.Tk()
root.withdraw()


# https://pillow.readthedocs.io/en/3.0.x/reference/Image.html
def load_image(address):
    """
    This function is just to fix intellisense.
    It's a much less efficient version of `Image.open(address)`
    """
    to_clone = Image.open(address)
    result = Image.new("RGB", (to_clone.width, to_clone.height))
    for x in range(result.width):
        for y in range(result.height):
            color = to_clone.getpixel((x, y))
            result.putpixel((x, y), color)

    return result


def prompt_user_for_image():
    file_path = filedialog.askopenfilename(filetypes=[("",".png"), ("",".jpg")])
    return load_image(file_path)

###########
# Everything above this can be ignored
###########


def image_update_template(loaded_image: Image.Image):
    clone = loaded_image.copy()  # load_image(file_path)
    for x in range(loaded_image.width):
        for y in range(loaded_image.height):
            color = loaded_image.getpixel((x, y))
            red = color[0]
            green = color[1]
            blue = 256 % (color[2]+1)
            new_color = (red, green, blue)
            clone.putpixel((x, y), new_color)
    return clone


loaded = prompt_user_for_image()
updated_image = image_update_template(loaded)
updated_image.show()
updated_image.save("demo.png")
