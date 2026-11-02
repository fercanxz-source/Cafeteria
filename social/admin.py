from django.contrib import admin
from .models import Redsocial

class RedsocialAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Redsocial, RedsocialAdmin)