from django import template
from django.utils import timezone

register = template.Library()


@register.simple_tag()
def remaining_time(due_date):
        time_left = due_date - timezone.now()
        return time_left


@register.filter()
def up_first_letter(value):
    first = value[0]
    remaining = value[1:]
    return first.upper() + remaining
