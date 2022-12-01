from django.urls import path
from . import views

urlpatterns = [
        path('', views.IndexView.as_view()),
        path('users', views.UserList.as_view(), name='users'),
        path('users/create', views.UserCreate.as_view(), name='user_create'),
]