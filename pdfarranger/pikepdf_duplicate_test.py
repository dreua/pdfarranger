import sys
import pikepdf

if len(sys.argv) < 2:
    print("Need one pdf as argument")
    exit(1)

pdf_output = pikepdf.Pdf.new()
pdf_input = pikepdf.open(sys.argv[1])

for i in range(4):
    pdf_output.pages.append(pdf_output.copy_foreign(pdf_input.pages[0]))

for i in [0,2]:
    pdf_output.pages[i].Rotate = 180

pdf_output.save("duplicate_pdf_test.pdf")
