from django.http import HttpResponseRedirect

from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Todo


class IndexView(generic.ListView):
    model = Todo
    template_name = 'todos/index.html'


class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todos/detail.html'


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return HttpResponseRedirect(reverse('todos:index'))


def create(request):
    todo = Todo(todo_text=request.POST["text"])
    todo.save()

    return HttpResponseRedirect(reverse('todos:index'))


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.todo_text = request.POST["text"]
    todo.save()

    return HttpResponseRedirect(reverse('todos:index'))
