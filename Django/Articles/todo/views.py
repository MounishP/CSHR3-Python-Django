from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo.models import Todo

# Create your views here.
def Todo_List(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo.html',{'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('Description')

        print(title,description)

        Todo.objects.create(title=title, description=description)
        return redirect('Todo_List')
    

def delete_todo(request, todo_id):
    todo=Todo.objects.get(id=todo_id)
    print(todo)
    todo.delete()
    return redirect('Todo_List')

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.progress=True
    todo.save()
    return redirect('Todo_List')

