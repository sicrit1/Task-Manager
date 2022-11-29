from django.urls import path
from . import views

urlpatterns = [
        path('', views.IndexView.as_view()),
        path('love/', views.LoveIt.as_view()),
]