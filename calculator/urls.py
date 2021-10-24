from django.urls import path
from . import views
from .views import SoapService

urlpatterns = [
    path('',views.home,name='calcul'),
    path('sum', SoapService.sum, name='sum'),
    path('mult', SoapService.mult, name='mult'),
    path('sub', SoapService.sub, name='sub'),
    path('div', SoapService.div, name='div'),
    path('powy', SoapService.powy, name='powy'),
    path('pow2', SoapService.pow2, name='pow2'),
    path('pow3', SoapService.pow3, name='pow3'),
    path('inver', SoapService.inver, name='inver'),
    path('sqrt2', SoapService.sqrt2, name='sqrt2'),
    path('sqrt3', SoapService.sqrt3, name='sqrt3'),
    path('sqrty', SoapService.sqrty, name='sqrty'),
]
