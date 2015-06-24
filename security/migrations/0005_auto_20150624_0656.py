# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0004_auto_20150623_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmasa',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, db_index=True),
        ),
        migrations.AlterField(
            model_name='pmasa',
            name='updated',
            field=models.DateTimeField(help_text=b'Set this in case of major update to the entry', null=True, blank=True),
        ),
    ]
