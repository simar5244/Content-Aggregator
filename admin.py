from django.contrib import admin
from .models import *
 
admin.site.register(Content1)
admin.site.register(Content2)
admin.site.register(Content3)
admin.site.register(Content4)


#superuser
py manage.py createsuperuser
