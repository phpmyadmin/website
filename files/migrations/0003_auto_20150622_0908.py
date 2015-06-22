# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20150622_0904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ['version_num']},
        ),
        migrations.AddField(
            model_name='release',
            name='version_num',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='version',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
