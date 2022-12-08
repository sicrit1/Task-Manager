from django.urls import path
from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks'),
    path('create', views.TasksCreate.as_view(), name='tasks_create'),
    path('<int:id>/update', views.TasksUpdate.as_view(), name='tasks_update'),
    path('<int:id>/delete', views.TasksDelete.as_view(), name='tasks_delete'),
]
