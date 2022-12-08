from django.urls import path
from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks'),
    path('create', views.TasksCreate.as_view(), name='tasks_create'),
    path('<int:id>/update', views.TasksUpdate.as_view(), name='tasks_update'),
    path('<int:id>/delete', views.TasksDelete.as_view(), name='tasks_delete'),


    # GET /tasks/ - страница со списком всех задач
    # GET /tasks/create/ - страница создания задачи
    # POST /tasks/create/ - создание новой задачи
    # GET /tasks/<int:pk>/update/ - страница редактирования задачи
    # POST /tasks/<int:pk>/update/ - обновление задачи
    # GET /tasks/<int:pk>/delete/ - страница удаления задачи
    # POST /tasks/<int:pk>/delete/ - удаление задачи
    # GET /tasks/<int:pk>/ - страница просмотра задачи

    # path('', views.StatusesView.as_view(), name='statuses'),
    # path('create', views.StatusesCreate.as_view(), name='statuses_create'),
    # path('<int:id>/update', views.StatusesUpdate.as_view(), name='statuses_update'),
    # path('<int:id>/delete', views.StatusesDelete.as_view(), name='statuses_delete'),
]
