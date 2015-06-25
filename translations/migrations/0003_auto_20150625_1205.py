# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0002_auto_20150625_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
