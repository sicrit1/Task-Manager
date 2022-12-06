from django.urls import path
from . import views


app_name = 'statuses'
urlpatterns = [
    path('', views.StatusesView.as_view(), name='statuses'),
    path('create', views.StatusesCreate.as_view(), name='statuses_create'),
    path('<int:id>/update', views.StatusesUpdate.as_view(), name='statuses_update'),
    path('<int:id>/delete', views.StatusesDelete.as_view(), name='statuses_delete'),
]
