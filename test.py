from PIL import Image, ImageFilter

img = Image.open("./image/bulbasaur.jpg")
print(img)

filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save("blur.png", 'png')

convert_image = img.convert("L")
convert_image.save("grey.png", 'png')

resize_image = img.resize((100,100))
resize_image.save('resized_image.png', 'png')