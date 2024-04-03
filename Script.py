import os
import img2pdf

images = []
for img_file in os.listdir("./img"):
    if img_file.endswith(".jpg"):
        with open(os.path.join("./img", img_file), "rb") as f:
            images.append(f.read())

with open("PetReport.pdf", "wb") as file:
    file.write(img2pdf.convert(images))
