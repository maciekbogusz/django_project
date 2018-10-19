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

