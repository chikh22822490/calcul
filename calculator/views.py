from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from spyne.model.primitive.number import NonNegativeInteger, PositiveInteger
from spyne.service import ServiceBase
from spyne.decorator import rpc 
from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.model.primitive import Double
import math

def home(request):
    return render(request, 'calcul.html', {'name':'calculator'})

class SoapService(ServiceBase):
    def sum(request): 
        x = int(request.GET['X'])
        y = int(request.GET['Y'])
        res = x + y
        return render(request, "calcul.html", {'result':res})
    
    def sub(request):
        x = int(request.GET['X'])
        y = int(request.GET['Y'])
        res = x-y
        return render(request, "calcul.html", {'result':res})

    def div(request):
        x = int(request.GET['X'])
        y = int(request.GET['Y'])
        res = x/y
        return render(request, "calcul.html", {'result':res})
    
    def mult(request):
        x = int(request.GET['X'])
        y = int(request.GET['Y'])
        res = x*y
        return render(request, "calcul.html", {'result':res})
    
    def powy(request):
        x = int(request.GET['X'])
        y = int(request.GET['Y'])
        res = math.pow(x,y)
        return render(request, "calcul.html", {'result':res})

    def pow2(request):
        x = int(request.GET['X'])
        res = x**2
        return render(request, "calcul.html", {'result':res})
    
    def pow3(request):
        x = int(request.GET['X'])
        res = x**3
        return render(request, "calcul.html", {'result':res})
    
    def sqrt2(request):
        x = int(request.GET['X'])
        res = math.sqrt(x)
        return render(request, "calcul.html", {'result':res})

    def sqrt3(request):
        x = int(request.GET['X'])
        res = x**(1/3)
        return render(request, "calcul.html", {'result':res})

    def sqrty(request):
        x = int(request.GET['X'])
        y = int(request.GET['Y'])
        res = x**(1/y)
        return render(request, "calcul.html", {'result':res})
    
    def inver(request):
        x = int(request.GET['X'])
        y = int(request.GET['Y'])
        res = 1/x
        return render(request, "calcul.html", {'result':res})
    
my_calculator= Application(
    [SoapService],
    tns='isg.soa.calculator',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

djangoCalcul= DjangoApplication(my_calculator)

my_soap_application = csrf_exempt(djangoCalcul)
