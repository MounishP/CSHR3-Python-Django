from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def homepage(request):
    cars = ['BMW','audi','swift']    
    return render(request,'index.html',{"cars":cars})

def about(request):
    return render(request, 'about.html',{"name":"Sampath"})

def cars(request):
    cars = {
        "cars":['bmw','audi','swift']
    }
    return JsonResponse(cars, safe=False)