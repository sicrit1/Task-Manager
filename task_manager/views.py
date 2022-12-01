from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import get_user_model
from task_manager.forms import UserForm

User = get_user_model()



class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'task_manager/index.html')


class UserList(View):

    def get(self, request, *args, **kwargs):
        user_list = User.objects.all()
        context = {'user_list': user_list}
        return render(request, 'task_manager/user_list.html', context=context)


class UserCreate(View):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'task_manager/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        return render(request, 'task_manager/create.html', {'form': form})
