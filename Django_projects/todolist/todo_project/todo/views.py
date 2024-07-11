from django.shortcuts import render, redirect

# Create your views here.
from .models import Todo
from .forms import TodoForm


def index(request):
    todos = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'todo/index.html', {'todos': todos, 'form': form})


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
