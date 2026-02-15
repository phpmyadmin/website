from django.contrib import admin
from demo.models import Demo


@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ('name', 'master_version')

