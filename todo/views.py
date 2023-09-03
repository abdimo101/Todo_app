from django.shortcuts import render
from todo.models import Todo
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos }
    return render(request, 'todo/index.html', context)
