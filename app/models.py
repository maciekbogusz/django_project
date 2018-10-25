import os
from django.conf import settings

class Stock(object):
    def __init__(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
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