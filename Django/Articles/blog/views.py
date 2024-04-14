from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    # return HttpResponse("This is a Homepage!!")   
    listNum = [1,2,3,4,5]
    return render(request,'index.html', {"listNum":listNum})

def about(request):
    return render(request, 'about.html',{"name":"Sampath"})