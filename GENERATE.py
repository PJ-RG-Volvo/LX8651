import string
import PIL
from PIL import Image, ImageDraw, ImageFont

S = 681

img = Image.new('RGB', (400, 100), color=(255, 255, 255))

d = ImageDraw.Draw(img)
fnt = ImageFont.truetype('StrOrBytesPath', 40)
d.text((50, 25), "Hello from Python!", font=fnt, fill=(0, 0, 0)) # Black text
img.save('text_on_image.png')
