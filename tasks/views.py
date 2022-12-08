from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model


from .models import Tasks
from statuses.models import Statuses


User = get_user_model()


class TasksView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        tasks_list = Tasks.objects.all()
        context = {'tasks_list': tasks_list}
        return render(request, 'tasks/tasks_list.html', context=context)


class TasksCreate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        statuses_list = Statuses.objects.all()
        user_list = User.objects.all()
        context = {
            'statuses_list': statuses_list,
            'user_list': user_list,
        }
        return render(request, 'tasks/task_create.html', context=context)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        executor_id = request.POST['executor']
        status_id = request.POST['status']
        # author = User.objects.get(id=request.user.id)
        task = Tasks.objects.create(
            name=name,
            description=description,
            status_id=status_id,
            executor_id=executor_id,
            author_id=request.user.id,
        )
        messages.add_message(request, messages.SUCCESS, f'The task was created successfully')
        return redirect('tasks:tasks')


class TasksUpdate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Tasks.objects.get(id=task_id)
        statuses_list = Statuses.objects.all()
        user_list = User.objects.all()
        context = {
            'statuses_list': statuses_list,
            'user_list': user_list,
            'task': task,
        }
        return render(request, 'tasks/update_tasks.html', context=context)

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Tasks.objects.get(id=task_id)
        name = request.POST['name']
        description = request.POST['description']
        executor = User.objects.get(id=request.POST['executor'])
        status = Statuses.objects.get(id=request.POST['status'])

        task.name = name
        task.description = description
        task.status = status
        task.executor = executor
        task.author = request.user
        task.save()
        messages.add_message(request, messages.SUCCESS, f'The task was updated successfully')
        return redirect('tasks:tasks')


class TasksDelete(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Tasks.objects.get(id=task_id)
        return render(request, 'tasks/tasks_delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Tasks.objects.get(id=task_id)
        if task:
            task.delete()
        return redirect('tasks:tasks')
