import PyPDF2
from googletrans import Translator
exam=[]
d=input("Enter the path address with name of the PDF file : ")
pdfFileObj = open(d, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
x=pdfReader.numPages
pageObj = pdfReader.getPage(0)
file=pageObj.extractText()
translator=Translator()
dfg=file.splitlines()
for p in dfg:
    translated=translator.translate(text=p,dest='en')
    exam.append(translated.text)
    print(translated.text)
pdfFileObj.close()
drop=open('write.txt','a', encoding="utf-8")
for i in exam:
    drop.writelines(i)
    drop.write("\n")
drop.close()
