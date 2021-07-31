from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import *


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):  # new
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['overdue_list'] = Task.objects.overdue_status()
        print(context)
        return context


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_new.html'
    fields = ('title', 'description', 'priority', 'group', 'due_date')
    success_url = reverse_lazy("task_list")


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class CategoryView(ListView):
    model = Categories
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):  # new
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['cat_empty'] = Categories.objects.empty_task()
        context['cat_full'] = Categories.objects2.full_task()
        print(context)
        return context


class CategoriesDetailView(DetailView):  # new
    context_object_name = 'categories_detail'
    model = Categories
    template_name = 'categories_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesDetailView, self).get_context_data(**kwargs)
        context['cat_list'] = Categories.objects.all()
        print(context)
        return context