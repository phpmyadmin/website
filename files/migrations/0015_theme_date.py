# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0014_auto_20150623_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
