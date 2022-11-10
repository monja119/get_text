import os
import pandas as pd
from PIL import Image
from pytesseract import pytesseract
from cutter import Cutter
from writter import Excel
import pdftables_api

class Main:
    def __init__(self, tesseract_path, name, image, col, row):
        # CUTTING IMAGES
        global data_ready
        type = image.split('.')[-1]
        cut_image(name, image, col, row)

        # EXTRACTING TEXTS
        # image name
        # Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = tesseract_path

        # Open image with PIL
        data = []
        print("> Extracting Data From Image : {}.{} ...".format(name, type))
        n = 1
        text = ''
        for i in range(n):
            progess = int((i / n) * 100)
            print("> {} % ".format(progess))
            path_to_image = '{}/{}_{}.{}'.format(name, name, i, type)
            img = Image.open(path_to_image)

            content = pd.DataFrame()
            text = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
            with open('test.pdf', 'w+b') as f:
                f.write(text)
            import tabula

            df = tabula.read_pdf("test.pdf", pages=1)[0]
            df.to_excel('here.xlsx')


def cut_image(name, image, col, row):
    Cutter(name, image, col, row)


if __name__ == "__main__":
    path_to_tesseract = r"C:\Users\monja\AppData\Local\Tesseract-OCR\tesseract.exe"
    extract = Main(path_to_tesseract, "test-gif", "images/gif.gif", 1, 100)
