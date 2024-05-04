from django.shortcuts import render, redirect
from menuApp.models import Menu
# Create your views here.
def index(request):
    return render(request, 'index.html');

def menu_list(request):
    menuItems = Menu.objects.all()
    return render(request, 'menu/menu_list.html',{'menuItems':menuItems})

def menu_details(request,pk):
    menu = Menu.objects.get(pk=pk)
    print(menu)
    return render(request, 'menu/menu_details.html',{'menu':menu})

def menu_delete(request, pk):
    menu = Menu.objects.get(pk=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    return render(request, 'menu/menu_confirm.html',{'menu':menu})