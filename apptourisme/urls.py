from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views
from .views import hotel,transport,restaurant,Visite_Create_View,Contact_Create_View,activite, Tanger,Assilah,Larache
from apptourisme.views import(index,)

urlpatterns = [

    path('hotel/', hotel, name='hotel'),
    path('restaurant/', restaurant, name='restaurant'),
    path('activite/', activite, name='activite'),
    path('transport/', transport, name='transport'),
    path('contact/', Contact_Create_View, name='contact'),
    path('visite/', Visite_Create_View, name='Visite'),
    path('Tanger/', Tanger, name='Tanger'),
    path('Assilah/', Assilah, name='Assilah'),
    path('Larache/', Larache, name='Larache'),
    path('', index),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
