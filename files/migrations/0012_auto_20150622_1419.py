# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0011_auto_20150622_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='release',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='release',
            name='visible',
        ),
        migrations.AlterField(
            model_name='release',
            name='stable',
            field=models.BooleanField(default=False, db_index=True),
        ),
    ]
