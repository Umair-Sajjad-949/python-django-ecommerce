from django.contrib import admin
from . import models

admin.site.register(models.Setting)
admin.site.register(models.Categories)
admin.site.register(models.Product)
