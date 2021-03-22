from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Todo


class IndexView(generic.ListView):
    model = Todo
    template_name = 'todos/index.html'


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return HttpResponseRedirect(reverse('todos:index'))


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('todo_text', 'todo_status')


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todos:index'))
    else:
        form = TodoForm()

    return render(request, 'todos/create.html', {'form': form})


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todos:index'))
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todos/detail.html', {"form": form})
