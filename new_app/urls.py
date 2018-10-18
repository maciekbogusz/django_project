from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^food/$', views.FoodPageView.as_view()),
    url(r'^stock/$', views.StockCheckerPageView.as_view()),
]