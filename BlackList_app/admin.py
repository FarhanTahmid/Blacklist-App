from django.contrib import admin

# Register your models here.
from.models import Complain, Users

admin.site.register(Users)
admin.site.register(Complain)