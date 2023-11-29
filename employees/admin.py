from django.contrib import admin
from .models import User, Sale, Finance, Technician
# Register your models here.


admin.site.register(User)
admin.site.register(Technician)
admin.site.register(Sale)
