from django.urls import path
from todo.views import Todo_List
from todo.views import create_todo,delete_todo,complete_todo

urlpatterns = [
    path('',Todo_List, name="Todo_List"),
    path('create', create_todo, name="create_todo"),
    path('delete/<int:todo_id>',delete_todo, name="delete_todo"),
    path('complete/<int:todo_id>',complete_todo,name="complete_todo"),
]


