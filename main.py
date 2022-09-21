from PIL import Image
from pytesseract import pytesseract
from cutter import Cutter


class Main:
    def __init__(self, tesseract_path, path_to_image):
        # Define path to image
        # Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = tesseract_path

        # Open image with PIL
        img = Image.open(path_to_image)

        # Extract text from image
        text = pytesseract.image_to_string(img)
        print(text)


if __name__ == "__main__":
    path_to_tesseract = r"C:\Users\monja\AppData\Local\Tesseract-OCR\tesseract.exe"
    path_to_image = "test.png"
    extract = Main(path_to_tesseract, path_to_image)
