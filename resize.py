from PIL import Image
import os, sys

path = "C:/Users/mcbg/workspace/dev/django_project/new_app/images/"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((100,100), Image.ANTIALIAS)
            imResize.save(f + '.png', 'png', quality=90)
resize()