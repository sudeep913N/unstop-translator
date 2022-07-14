import PyPDF2
from googletrans import Translator
pdfFileObj = open('tranlitrated_test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
x=pdfReader.numPages
pageObj = pdfReader.getPage(0)
file=pageObj.extractText()
translator=Translator()
dfg=file.splitlines()
for p in dfg:
    translated=translator.translate(text=p,dest='en')
    print(translated.text)
pdfFileObj.close()
