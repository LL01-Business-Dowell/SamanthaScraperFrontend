from django.contrib import admin
from .models import ScraperFile, Notifications

# Register your models here.
admin.site.register(ScraperFile)
admin.site.register(Notifications)