from PIL import Image
from pytesseract import pytesseract
from cutter import Cutter


# cutting file
cutter = Cutter("monja", "test.png", 1, 5)


# Define path to tessaract.exe
path_to_tesseract = r'C:/Users/monja/AppData/Local/Tesseract-OCR/tesseract.exe'

# Define path to image
path_to_image = 'test.png'

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Open image with PIL
img = Image.open(path_to_image)

# Extract text from image
text = pytesseract.image_to_string(img)
print(text)

