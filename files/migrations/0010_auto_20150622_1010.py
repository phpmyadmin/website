# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0009_auto_20150622_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='display_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
