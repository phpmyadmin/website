# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0013_auto_20150623_0638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='download',
            options={'ordering': ['-release__version_num', 'filename']},
        ),
        migrations.AddField(
            model_name='release',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
