from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Todo

# Create your views here.
def todolist(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo.html',{'todos':todos})