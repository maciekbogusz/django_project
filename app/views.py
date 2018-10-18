from django.shortcuts import render
from django.views.generic import TemplateView
from lxml import html
import requests
from app.models import Stock
# Create your views here.

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

class StockCheckerPageView(TemplateView):
        def get(self, request, **kwargs):
                my_stocks = {'PXM':None, 'NTT':None, 'ABC':None, 'BIO':None, 'CDR':None} 
                for keys in my_stocks:
                        newStock = Stock(keys)
                        stockPrice = get_data(newStock)
                        newStock.setPrice(stockPrice)
                        my_stocks[keys] = newStock.price
                return render(request, 'stock.html', { 'content': my_stocks })
        

        