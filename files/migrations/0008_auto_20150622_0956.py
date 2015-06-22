# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='slug',
        ),
        migrations.AlterField(
            model_name='theme',
            name='filename',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='theme',
            name='version',
            field=models.CharField(max_length=50),
        ),
    ]
