import pyPDF2
import pyttsx3
#pdf path
path=open('file.pdf','rb')
#pdf obyekti yarat
pdfReader=pyPDF2.PdfFileReader(path)
#nece sehife oxumaq lazim oldudugunu qeyd et
from_page=pdfReader.getPage(30)
#text xaric et
text=from_page.extractText()
#read text
speak=pyttsx3.init()
speak.say(text)
speak.runAndWait()