import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)


def image_to_string(filename=None, image=None):
    print("image to print {}".format(image))
    if filename:
        image = Image.open(filename)
    return pytesseract.image_to_string(image)