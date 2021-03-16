from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
    path('create', views.create, name='create'),
    path('<int:todo_id>/update', views.update, name='update')
]
