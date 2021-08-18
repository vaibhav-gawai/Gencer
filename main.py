from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from PIL import ImageFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A1, A4, letter
pdfmetrics.registerFont(TTFont('poppins', 'Fonts\Poppins-Bold.ttf'))


l = [] # list containing names
line = ""
with open('names.txt') as n:
    line+= n.readline()
l = line.split(",")
print(l)
pac = []

def retPac(l):
    for i in l:
        packet = io.BytesIO()
        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.saveState()
        can.setFont("poppins", 48)
        can.setFillColorRGB(14/256,69/256,115/266)
        # can.drawString(250,300, str(i))
        # can.drawString(290,260, "|")
        # can.drawString(800,260, "|")
        font = ImageFont.truetype("Fonts\Poppins-Bold.ttf", 48)
        # print(font)
        size = font.getsize(str(i))
        print(size[0])
        can.drawString(290+((510-size[0])/2),260, str(i))
        # can.restoreState()
        can.save()
        pac.append(packet)
    return pac


def start():
    packet = retPac(l)
    k = 0
    for i in packet:
        #move to the beginning of the StringIO buffer
        i.seek(0)
        new_pdf = PdfFileReader(i)
        # read your existing PDF
        existing_pdf = PdfFileReader(open("Templates/Canva2.pdf", "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        num = random.randint(1111,9999)
        outputStream = open("Output/"+l[k]+"_"+str(num)+".pdf", "wb")
        k+=1
        output.write(outputStream)
        outputStream.close()

start()