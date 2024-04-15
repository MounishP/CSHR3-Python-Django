from django.shortcuts import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("<h1>Hello, Welcome to Django Application!!</h1>")

def hello(request):
    return HttpResponse("<hr>Hello<hr>")