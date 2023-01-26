#import PyCryptodome
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
reader = PyPDF2.PdfReader(book)
pages = len(reader.pages)
for num in range(0, pages):
    page = reader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()