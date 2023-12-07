from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('submit/', views.submit),
    path('delete/<int:stu_id>', views.delete, name='delete_student'),
]