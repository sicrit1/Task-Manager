from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Labels


class LabelsView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        labels_list = Labels.objects.all()
        context = {'labels_list': labels_list}
        return render(request, 'labels/labels_list.html', context=context)


class LabelsCreate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        return render(request, 'labels/create_labels.html')

    def post(self, request, *args, **kwargs):
        label_name = request.POST['label_name']
        label = Labels(name=label_name)
        label.save()
        messages.add_message(request, messages.SUCCESS, f'The label was created successfully')
        return redirect('labels:labels')


class LabelsUpdate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Labels.objects.get(id=label_id)
        return render(request, 'labels/update_labels.html', {'label': label})

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Labels.objects.get(id=label_id)
        new_name = request.POST['name']
        label.name = new_name
        label.save()
        messages.add_message(request, messages.SUCCESS, f'The label was saved successfully')
        return redirect('labels:labels')


class LabelsDelete(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Labels.objects.get(id=label_id)
        return render(request, 'labels/delete_labels.html', {'label': label})

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Labels.objects.get(id=label_id)
        if label:
            label.delete()
        return redirect('labels:labels')
