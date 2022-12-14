from django.urls import path
from . import views

urlpatterns = [
        path('', views.IndexView.as_view(), name='home'),
        path('users', views.UserList.as_view(), name='users'),
        path('users/create', views.UserCreate.as_view(), name='user_create'),
        path('login', views.UserLogin.as_view(), name='login'),
        path('logout', views.UserLogout.as_view(), name='logout'),
        path('users/<int:id>/update', views.UserUpdate.as_view(), name='update'),
        path('users/<int:id>/delete', views.UserDelete.as_view(), name='delete'),
]
