from django.contrib import admin

# Register your models here.

from hello.models import Greeting

admin.site.register(Greeting)
