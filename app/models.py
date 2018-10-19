from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class Stock(object):
    def __init__(self, name):
        self.name = name
    
    def setPrice(self, price):
        self.price = price
            
    def getName(self):
        return self.name
        
    def getPrice(self):
        return self.price

# class Furnitures(models.Model):
#     pictures = models.ImageField(upload_to = image_directory_path, storage = image_storage )

class Furniture(object):
    def __init__(self, name):
        self.name = name

    def setWidth(self, width):
        self.width = width
    
    def setHeigth(self, heigth):
        self.heigth = heigth
    
    def getWidth(self):
        return self.width
    
    def getHeigth(self):
        return self.heigth


IMAGE_STORAGE = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/images/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}images/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'picture/{0}'.format(filename)


class Goods(models.Model):
    pic = models.ImageField(upload_to=image_directory_path, storage=IMAGE_STORAGE)
