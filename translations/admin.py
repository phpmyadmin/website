from django.contrib import admin
from translations.models import Translation


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('name', 'translated', 'percent', 'updated')

