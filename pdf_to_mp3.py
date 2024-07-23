from pytesseract import pytesseract
from pdf2image import convert_from_path

from gtts import gTTS 
import os

def read_pdf_page_as_str(filename, page=1):
    images = convert_from_path(filename)
    return pytesseract.image_to_string(images[page-1])

def read_pdf_as_str(filename, page_start=1, page_end=-1):
    images = convert_from_path(filename)
    text = ""
    for i in range(page_start - 1, len(images) if page_end < 1 else page_end):
        text += pytesseract.image_to_string(images[i])
        print(i)
    return text

def text_to_speech_google(text, path='temp.mp3'):
    speech = gTTS(text=' '.join(text.split()).replace('"', "\"").replace('\x00', ' '), lang='en', slow=False)
    speech.save(path)


in_path = '3442188.3445922.pdf'
out_path = 'temp.mp3'
text_to_speech_google(read_pdf_as_str(in_path, 1, 5), path=out_path)