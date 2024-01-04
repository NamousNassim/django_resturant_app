from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/' , views.aboutus , name='about_us'),
    path('book/' , views.booking , name='book_now'), 
    path('Menu/' , views.Menu , name='Menu')
    ]