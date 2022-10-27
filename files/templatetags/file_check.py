import os.path

from django import template
from django.templatetags.static import static
from django.conf import settings
from os import path

register = template.Library()

@register.filter(name='image_exists')

def image_exists(filepath):
    imagePath = settings.BASE_DIR+'/pmaweb/'+static(filepath);
    if path.exists(imagePath):
        return True
    else:
        return False
