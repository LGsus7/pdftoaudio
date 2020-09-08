#!/usr/bin/python
# -*- coding: latin-1 -*-
from Tkinter import Tk
from tkFileDialog import askopenfilename
import pdftotext
from gtts import gTTS

Tk().withdraw() # no queremos una GUI completa, asi que evita que aparezca la ventana raiz
filelocation = askopenfilename() # abre el cuadro de dialogo GUI

with open(filelocation, "rb") as f: # abre el archivo en modo lectura (rb) y lo llamamos f
	pdf= pdftotext.PDF(f)
string_of_text = ''
for text in pdf:
	string_of_text += text

final_file = gTTS(text=string_of_text, lang='es') # almacenar archivo en variable
final_file.save("Generated Speech.mp3") # guardar archivo e
