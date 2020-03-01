import sys
import pikepdf

if len(sys.argv) < 2:
    print("Need one pdf as argument")
    exit(1)

pdf_input = pikepdf.open(sys.argv[1])
pdf_output = pikepdf.Pdf.new()


for page in pdf_input.pages:
    for i in range(2):
        pdf_output.pages.append(pdf_output.copy_foreign(page))

is_left_page = True
for page in pdf_output.pages:
    x_start, y_start, x_end, y_end = page.MediaBox
    # page.MediaBox does not always start with [0, 0, ...] therefore we need
    # the following calculation to find the middle of the page
    middle = x_start + (x_end - x_start) / 2
    if is_left_page:
        x_end = middle
    else:
        x_start = middle
    page.MediaBox = [x_start, y_start, x_end, y_end]
    is_left_page = not is_left_page

pdf_output.save("crop_pdf.pdf")
