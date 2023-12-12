from django import template
from django.utils.timesince import timesince


from dateutil import relativedelta
from datetime import datetime, timedelta, timezone
register = template.Library()


@register.filter
def fivedaysago(value):
    now = datetime(datetime.now().year, datetime.now().month, datetime.now().day, tzinfo=timezone.utc)
    print(type(value), type(now))
    deta = now - value

    if deta < timedelta(days=5):
        return timesince(value) + ' ago'
    return value.strftime("%d-%m-%Y")


@register.filter
def months_since(value):
    try:
        now = datetime(datetime.now().year, datetime.now().month, datetime.now().day, tzinfo=timezone.utc)
        delta = relativedelta.relativedelta(dt1=now, dt2=value)
        time_slip = delta.years * 12 + delta.months
        return time_slip
    except ValueError:
        return 'Infinity'