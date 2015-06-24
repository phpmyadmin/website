# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0015_theme_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, db_index=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, db_index=True),
        ),
    ]
