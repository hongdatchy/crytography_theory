import base64

encoded_string = ""
with open("1.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    print(encoded_string)

imgdata = base64.b64decode(encoded_string)
filename = '2.png'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(imgdata)