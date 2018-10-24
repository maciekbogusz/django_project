import os
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
from lxml import html
import requests
from app.models import Stock, Furniture

def get_data(stock):
    lower_index = stock.name.lower()
    try:
        page = requests.get('https://stooq.pl/q/?s='+lower_index)
        tree = html.fromstring(page.content)
        price = tree.xpath('//span[@id="aq_'+lower_index+'_c2|3"]/text()')
        return price
    except requests.exceptions.ConnectionError:
        requests.status_codes = "Connection refused"
    
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"

class FoodPageView(TemplateView):
    template_name = "food.html"

class MovingView(TemplateView):   
    def get(self, request, **kwargs):
        furntiure = Furniture()
        image_list = furntiure.get_images()      
        dict_of_images = {i: image_list[i] for i in range(0, len(image_list))}
        return render(request, 'moving.html', {'content': dict_of_images})
    
    def getDataFromTable(self, request):
        print(request.POST)
                
class StockCheckerPageView(TemplateView):
    def get(self, request, **kwargs):
        my_stocks = {'PXM':None, 'NTT':None, 'ABC':None, 'BIO':None, 'CDR':None} 
        for keys in my_stocks:
            new_stock = Stock(keys)
            stock_price = get_data(new_stock)
            new_stock.setPrice(stock_price)
            my_stocks[keys] = new_stock.price
        return render(request, 'stock.html', { 'content': my_stocks})
     