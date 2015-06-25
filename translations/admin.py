from django.contrib import admin
from translations.models import Translation


class TranslationAdmin(admin.ModelAdmin):
    list_display = ('name', 'translated', 'percent', 'updated')

admin.site.register(Translation, TranslationAdmin)
