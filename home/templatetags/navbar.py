from django import template
from  home.models import  User
register = template.Library()

@register.inclusion_tag('navbar.html')
def show_menu():
    return {'users':User.objects.all()}
