from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _


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
        return render(request, 'task_manager/create.html')

    def post(self, request, *args, **kwargs):
        user_list = list(User.objects.values_list('username', flat=True))
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if username in user_list:
            messages.add_message(request, messages.WARNING, _(f'A user with the same username already exists'))
            return redirect('user_create')
        if password1 != password2:
            messages.add_message(request, messages.WARNING, _(f'Passwords are not the same'))
            return redirect('user_create')
        user = User.objects.create_user(username, password=password1, first_name=first_name, last_name=last_name)
        messages.add_message(request, messages.SUCCESS, _(f'User {user.username} was create successfully'))
        return redirect('login')


class UserLogin(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'task_manager/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.WARNING, _("Username or password doesn't correct"))
            return redirect('login')


class UserLogout(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class UserUpdate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        return render(request, 'task_manager/update.html', {'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        user_list = list(User.objects.values_list('username', flat=True))
        new_username = request.POST['username']
        new_first_name = request.POST['first_name']
        new_last_name = request.POST['last_name']
        if new_username in user_list and new_username != user.username:
            messages.add_message(request, messages.WARNING, _(f'A user with the same username already exists'))
            return redirect('update', user.id)
        user.username = new_username
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.save()
        messages.add_message(request, messages.SUCCESS, _(f'The User {user.username} was updated successfully'))
        return redirect('users')


class UserDelete(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        return render(request, 'task_manager/delete.html', {'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('users')
