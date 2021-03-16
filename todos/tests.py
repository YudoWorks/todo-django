from django.test import TestCase
from django.urls import reverse

from .models import Todo


class TodoIndexViewTest(TestCase):
    def test_todo(self):
        Todo.objects.create(todo_text="Todo 1")
        response = self.client.get(reverse('todos:index'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['todo_list'], ['<Todo: Todo 1>'])
