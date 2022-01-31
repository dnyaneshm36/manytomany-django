from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)