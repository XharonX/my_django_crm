from django import template
from ..models import Department
from django.template.loader import get_template

register = template.Library()


def show_departments():
   departments = Department.objects.all()
   return {'departments': departments}


t = get_template('components/departments.html')
register.inclusion_tag(t)(show_departments)
