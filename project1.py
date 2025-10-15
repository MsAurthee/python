
from PyPDF2 import PdfMerger

AllPDF = [
    "pdf1.pdf",
    "pdf2.pdf",
    "pdf3.pdf",

]

OurMerger = PdfMerger()

for pdf in AllPDF:
    OurMerger.append(pdf)

OurMerger.write("output.pdf")
OurMerger.close()
