from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Statuses


class StatusesView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        statuses_list = Statuses.objects.all()
        context = {'statuses_list': statuses_list}
        return render(request, 'statuses/statuses_list.html', context=context)


class StatusesCreate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        return render(request, 'statuses/create_status.html')

    def post(self, request, *args, **kwargs):
        status_name = request.POST['status_name']
        statuses = Statuses(name=status_name)
        statuses.save()
        messages.add_message(request, messages.SUCCESS, f'Статус успешно создан')
        return redirect('statuses')
class StatusesUpdate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Statuses.objects.get(id=status_id)
        return render(request, 'statuses/update_statuses.html', {'status': status})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Statuses.objects.get(id=status_id)
        new_name = request.POST['name']
        status.name = new_name
        status.save()
        messages.add_message(request, messages.SUCCESS, f'Статус успешно изменен')
        return redirect('statuses:statuses')


class StatusesDelete(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Statuses.objects.get(id=status_id)
        return render(request, 'statuses/delete_statuses.html', {'status': status})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Statuses.objects.get(id=status_id)
        if status:
            status.delete()
        return redirect('statuses:statuses')
