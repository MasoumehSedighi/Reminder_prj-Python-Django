from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('new/', TaskCreateView.as_view(), name='task_new'),
    path('list/', TaskListView.as_view(), name='task_list'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('details/<str:pk>/', CategoriesDetailView.as_view(), name='categories_detail'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),


]