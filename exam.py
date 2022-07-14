import PyPDF2
from googletrans import Translator
pdfFileObj = open('bihar.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
x=pdfReader.numPages
pageObj = pdfReader.getPage(0)
file=pageObj.extractText()
translator=Translator()
for p in range(x):
    translated=translator.translate(text=file,dest='te')
    data=str(translated)
pdfFileObj.close()
drop=open('write.txt','a', encoding="utf-8")
for i in data:
    drop.writelines(i)
drop.close()
