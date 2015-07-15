from django.contrib import admin
from demo.models import Demo


class DemoAdmin(admin.ModelAdmin):
    list_display = ('name', 'master_version')

admin.site.register(Demo, DemoAdmin)
