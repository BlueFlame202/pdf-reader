from pytesseract import pytesseract
from pdf2image import convert_from_path

from gtts import gTTS 
import os

from threading import Thread

LIBRARY = {
    0 : '/Users/aathreyakadambi/Zotero/storage/C7AKZCEM/Dery et al. - Neural Combinatorial Optimization for Solving Jigs.pdf',
    'H&P' : '/Users/aathreyakadambi/MEGA/MEGAsync/Books/Computer Science/Architecture/Computer Architecture A Quantitative Approach (5th edition).pdf'
}

def get_pdf_page_len(filename):
    images = convert_from_path(filename)
    return len(images)

def read_pdf_page_as_str(filename, page=1):
    images = convert_from_path(filename)
    return pytesseract.image_to_string(images[page-1])

def text_to_speech_google(text):
    speech = gTTS(text=' '.join(text.split()).replace('"', "\"").replace('\x00', ' '), lang='en', slow=False)
    speech.save('temp.mp3')
    #def task():
    os.system('afplay temp.mp3')
    #thread = Thread(target=task)
    #thread.start()

def text_to_speech_mac(text):
    #def task():
    os.system("say " + "-v " + "\"" + "Tom" + "\" \"" + ' '.join(text.split()).replace('"', "\"").replace('\x00', ' ') + "\" -r " + str(175))
    #thread = Thread(target=task)
    #thread.start()

pdf_path = LIBRARY['H&P']
page_curr = 75
page_end = get_pdf_page_len(pdf_path) - 1

while page_curr < page_end:
    to_speak = read_pdf_page_as_str(pdf_path, page_curr)
    print(to_speak)
    print('page: ', page_curr)
    if (to_speak != ''):
        print('here')
        text_to_speech_mac(to_speak)
    page_curr += 1