import PyPDF2 as pdf

pdf_files = ['1.pdf', '2.pdf', '3.pdf', '4.pdf']  # name of the pdf files you want to merge
merger = pdf.PdfMerger()

for files in pdf_files:
    raw_files = open(files, 'rb')  # rb is reading but for binary files
    pdf_reader = pdf.PdfReader(raw_files)
    merger.append(pdf_reader)

# noinspection PyUnboundLocalVariable
raw_files.close()
merger.write('merged.pdf')  # name of the final and merged pdf
