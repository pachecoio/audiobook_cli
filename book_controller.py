import os
import pyttsx3
from pdf2image import convert_from_path
from tesseract import image_to_string


class BookException(Exception):
    message = "Error found"

    def __init__(self, message):
        self.message = message


class BookController(object):
    poppler_path = r"C:\\poppler\\bin"
    speaker = None
    images = []

    def __init__(self, images=None, filename=None):
        self.speaker = pyttsx3.init()

        if filename:
            filepath = os.path.join("books", filename)
            print("Filepath: {}".format(filepath))
            self.images = convert_from_path(filepath, poppler_path=self.poppler_path)

        if not self.images:
            raise BookException(message="No images found")

        print("{} images found".format(len(self.images)))

    def read_page(self, page):
        print("Print page {}".format(page))
        print("{} images found".format(len(self.images)))
        image = self.images[page]
        print('print image {}'.format(image))
        text = image_to_string(image=image)
        content = text.replace("\n", " ")
        print("Text found: \n {}".format(content))
        self.speaker.say(content)

    def run(self):
        self.speaker.runAndWait()
