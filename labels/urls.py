from django.urls import path
from . import views


app_name = 'labels'
urlpatterns = [
    path('', views.LabelsView.as_view(), name='labels'),
    path('create', views.LabelsCreate.as_view(), name='labels_create'),
    path('<int:id>/update', views.LabelsUpdate.as_view(), name='labels_update'),
    path('<int:id>/delete', views.LabelsDelete.as_view(), name='labels_delete'),
]
