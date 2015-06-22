# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20150622_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
