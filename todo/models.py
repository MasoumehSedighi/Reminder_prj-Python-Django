import datetime
from django.db import models
from django.db.models import Count
from django.urls import reverse
from django.db.models.functions import Coalesce


# Create your models here.
class EmptyList(models.Manager):
    def empty_task(self):
        return self.annotate(num_responses=Coalesce(models.Count("task"), 0)).filter(num_responses__lt=1)


class FullList(models.Manager):
    def full_task(self):
        return self.annotate(num_responses=Coalesce(models.Count("task"), 0)).filter(num_responses__gt=0)


class Categories(models.Model):
    categories_name = models.CharField(max_length=20, primary_key=True)
    objects = EmptyList()
    objects2 = FullList()

    def __str__(self):
        return self.categories_name

    class Meta:
        ordering = ["categories_name"]
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("categories_detail", kwargs={'pk': self.pk})


class OverDueManager(models.Manager):
    def overdue_status(self):
        return self.filter(due_date__lt=datetime.date.today())


class Task(models.Model):
    title = models.CharField(max_length=255)
    group = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True, null=True)
    priority = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    objects = OverDueManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["due_date"]

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])
