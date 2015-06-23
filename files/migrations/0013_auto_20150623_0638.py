# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0012_auto_20150622_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='md5',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='sha1',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='signed',
            field=models.BooleanField(default=False),
        ),
    ]
