image_list = sorted(Path("screens").glob("*.png"))

with open("ebook_output.pdf", "wb") as f:
    f.write(img2pdf.convert([str(img) for img in image_list]))

print("PDF yaratildi: ebook_output.pdf")
