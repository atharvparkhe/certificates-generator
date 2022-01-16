from PIL import Image, ImageDraw, ImageFont

names = ["Atharv Parkhe", "Abhinav Borde", "Sairaj Rasam"]

font = ImageFont.truetype("font.ttf", 100)

for i in names:
    img = Image.open("certificate.jpg")
    draw = ImageDraw.Draw(img)
    draw.text(xy=(800, 630), text=i, fill=(0,0,0), font=font)
    img.save("folder/" + i + " certificate" + ".jpg")