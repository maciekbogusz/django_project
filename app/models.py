from django.db import models

# Create your models here.
class Stock(object):
    def __init__(self, name):
        self.name = name
    
    def setPrice(self, price):
        self.price = price
            
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price