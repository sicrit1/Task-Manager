from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model


from .models import Tasks
from statuses.models import Statuses
from labels.models import Labels


User = get_user_model()


class TasksView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        tasks_list = self.filter()
        statuses_list = Statuses.objects.all()
        user_list = User.objects.all()
        labels_list = Labels.objects.all()
        context = {
            'statuses_list': statuses_list,
            'user_list': user_list,
            'labels_list': labels_list,
            'tasks_list': tasks_list,
        }
        return render(request, 'tasks/tasks_list.html', context=context)

    def filter(self):
        status_id = self.request.GET.get('status')
        executor_id = self.request.GET.get('executor')
        labels = self.request.GET.getlist('label')
        print(self.request.GET)
        qs = Tasks.objects.all()
        if status_id:
            qs = qs.filter(status_id=status_id)
        if executor_id:
            qs = qs.filter(executor_id=executor_id)
        if labels:
            qs = qs.filter(labels__in=labels)
        return qs


class TasksCreate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        statuses_list = Statuses.objects.all()
        user_list = User.objects.all()
        labels_list = Labels.objects.all()
        context = {
            'statuses_list': statuses_list,
            'user_list': user_list,
            'labels_list': labels_list,
        }
        return render(request, 'tasks/task_create.html', context=context)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description']
        executor_id = request.POST['executor']
        status_id = request.POST['status']
        label_list = request.POST.getlist('label')
        labels = Labels.objects.filter(id__in=label_list)
        task = Tasks.objects.create(
            name=name,
            description=description,
            status_id=status_id,
            executor_id=executor_id,
            author_id=request.user.id,
        )
        task.labels.add(*list(labels))
        messages.add_message(request, messages.SUCCESS, f'The task was created successfully')
        return redirect('tasks:tasks')


class TasksUpdate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Tasks.objects.get(id=task_id)
        statuses_list = Statuses.objects.all()
        user_list = User.objects.all()
        labels_list = Labels.objects.all()
        context = {
            'statuses_list': statuses_list,
            'user_list': user_list,
            'task': task,
            'labels_list': labels_list,
        }
        return render(request, 'tasks/update_tasks.html', context=context)

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Tasks.objects.get(id=task_id)
        name = request.POST['name']
        description = request.POST['description']
        executor = User.objects.get(id=request.POST['executor'])
        status = Statuses.objects.get(id=request.POST['status'])
        label_list = request.POST.getlist('label')
        labels = Labels.objects.filter(id__in=label_list)

        task.name = name
        task.description = description
        task.status = status
        task.executor = executor
        task.author = request.user
        task.labels.add(*list(labels))
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
