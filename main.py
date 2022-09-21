import os
from PIL import Image
from pytesseract import pytesseract
from cutter import Cutter


class Main:
    def __init__(self, tesseract_path, name, image, col, row):
        # CUTTING IMAGES
        cut_image(name, image, col, row)

        # EXTRACTING TEXTS
        # image name
        # Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = tesseract_path

        # Open image with PIL
        for i in range(row):
            path_to_image = '{}/{}_{}.png'.format(name, name, i)
            img = Image.open(path_to_image)
            # Extract text from image
            text = pytesseract.image_to_string(img)
            print(text)


def cut_image(name, image, col, row):
    Cutter(name, image, col, row)


if __name__ == "__main__":
    path_to_tesseract = r"C:\Users\monja\AppData\Local\Tesseract-OCR\tesseract.exe"
    extract = Main(path_to_tesseract, "monja", "this.png", 1, 100)
