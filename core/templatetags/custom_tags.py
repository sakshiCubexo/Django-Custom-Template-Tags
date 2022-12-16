from django import template
import datetime
from django.template.defaultfilters import stringfilter
from django.template.loader import get_template
from django.contrib.auth.models import User

register = template.Library()

@register.filter
@stringfilter
def func_lower(value):
    return value.lower()

@register.filter
@stringfilter
def func_title(value):
    return value.title()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.inclusion_tag('core/users.html')
def show_users_table():
    users = User.objects.all()
    return {'users': users}