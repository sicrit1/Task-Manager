from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login

from task_manager.forms import UserForm, LoginUserForm


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
            messages.add_message(request, messages.SUCCESS, 'User was created successfully')
            return redirect('login')
        messages.add_message(request, messages.WARNING, "User didn't create")
        return render(request, 'task_manager/create.html', {'form': form})


class UserLogin(View):

    def get(self, request, *args, **kwargs):
        form = LoginUserForm()
        return render(request, 'task_manager/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginUserForm()
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.add_message(request, messages.WARNING, 'Invalid user')
                return redirect('login')
        else:
            messages.add_message(request, messages.WARNING, "Username or password doesn't correct")
            return redirect('login')
