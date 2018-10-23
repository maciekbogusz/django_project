import os
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

class Furniture(object):
    
    def get_images(self):
        image_list = []
        static_dirs = settings.STATICFILES_DIRS
        for directory in static_dirs:
            for file in os.listdir(directory):
                if file.endswith(".png"):
                    image_list.append(file)      
        return image_list