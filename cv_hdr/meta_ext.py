import PIL.Image
from PIL.ExifTags import TAGS

img = PIL.Image.open('2933.jpg')
# meta = img.getexif()
meta = img._getexif()
print(f'{type(meta)}')

for key,value in meta.items():

    tag = TAGS.get(key, key)

    print(f'{key:10}/{tag:30}: {value}')




