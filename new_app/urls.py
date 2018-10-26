from django.conf.urls import url, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^food/$', views.FoodPageView.as_view()),
    url(r'^stock/$', views.StockCheckerPageView.as_view()),
    url(r'^moving/$', views.MovingView.as_view()),
    url(r'^form/$', views.FormView.as_view()),   
    url(r'^your-name/$', views.FormView.as_view()),   
]