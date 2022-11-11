import os, warnings
import tabula
from PIL import Image
from pytesseract import pytesseract
from cutter import Cutter


class Main:
    def __init__(self, tesseract_path, file_path, name, cut):
        # Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = tesseract_path
        Image.MAX_IMAGE_PIXELS = None

        # Reading image
        image_type = file_path.split('.')[-1]
        Cutter(name, file_path, 1, cut)  # cutting image

        print("> Opening file : {}".format(file_path))

        print("> Reading Data from file... ")
        for i in range(cut):
            if i == 0:
                print('~ Please, wait : Building {}/{}_{}.xlsx'.format(name, name, i))  # percentage
            else:
                print('~ {}% : Building {}/{}_{}.xlsx'.format((i * 100) // cut, name, name, i))  # percentage

            new_xlsx = '{}/{}_{}.xlsx'.format(name, name, i)  # stocking data
            new_pdf = '{}/{}_{}.pdf'.format(name, name, i)
            new_image = '{}/{}_{}.{}'.format(name, name, i, image_type)

            # opening each files
            image = Image.open(new_image)
            text = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')  # converting data to pdf

            # creating new pdf
            with open(new_pdf, 'w+b') as f:
                f.write(text)   # merging two io Bytes data ?

            # extracting data from new pdf
            try:
                data = tabula.read_pdf(new_pdf, pages=1)[0]
                data.to_excel(new_xlsx)
            except IndexError:
                print('Sorry, your image is too shorter or does not contain Text data. try to increase its size \n ')

            #   removing no sense files
            os.remove(new_pdf)

        for k in range(cut):
            new_image = '{}/{}_{}.{}'.format(name, name, k, image_type)
            os.remove(new_image)

        print('~ 100%')
        print('> Success in {}/'.format(name))


if __name__ == "__main__":
    path_to_tesseract = r"C:\Users\monja\AppData\Local\Tesseract-OCR\tesseract.exe"
    extract = Main(path_to_tesseract, 'gif.gif', "this", 2)

