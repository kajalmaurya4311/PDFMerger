from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("pdf1.pdf")
writer = PdfWriter()

# Loop through all pages
for page in reader.pages:
    page.rotate(180)   # rotate each page by 90 degrees
    writer.add_page(page)

# Save output file
with open("output1.pdf", "wb") as fp:
    writer.write(fp)

print("All pages rotated and saved to output.pdf")