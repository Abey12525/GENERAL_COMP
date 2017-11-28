import requests as rq
URL=input("paste the URL here : ")
for i in range(1,88):
	url = "https://image.slidesharecdn.com/ss4-150121113221-conversion-gate02/95/ss4-{}-1024.jpg?cb=1421861715".format(i)
	image_name = '{}.jpg'.format(i)
	r = rq.get(url, stream=True)
	with open(image_name, 'wb') as f:
		for chunk in r.iter_content():
			f.write(chunk)
			

from PyPDF2 import PdfFileWriter, PdfFileReader,PdfFileMerger		
from fpdf import FPDF
from PIL import Image
import glob
import os
import sys 
import subprocess as sp
cwd=os.getcwd()
image_directory = '{}'.format(cwd)
pdf_dir='{}'.format(cwd)
margin = 10
imagelist=[] 
pdf_list=[]	
merger = PdfFileMerger()
for i in range(1,88):
	str=cwd+"{}{}.jpg".format('\\',i)
	imagelist.append(str)
	
for imagePath in imagelist:
	cover = Image.open(imagePath)
	width, height = cover.size
	pdf = FPDF(unit="pt", format=[width + 2*margin, height + 2*margin])
	pdf.add_page()
	pdf.image(imagePath, margin, margin)
	destination = os.path.splitext(imagePath)[0]
	pdf.output(destination + ".pdf", "F")
	str=destination+ '.pdf'
	pdf_list.append(str)
	
for f in pdf_list:
	merger.append(PdfFileReader(f), 'rb')
	
	
filename=input("Enter the file name : ")
merger.write(filename+".pdf")

for i in range(1,88):
	os.system("del {}.jpg".format(i))
	os.system("del {}.pdf".format(i))


