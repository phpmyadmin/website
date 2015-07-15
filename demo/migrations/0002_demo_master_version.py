# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='master_version',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
