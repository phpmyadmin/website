# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0010_auto_20150622_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ['-version_num']},
        ),
        migrations.AddField(
            model_name='release',
            name='stable',
            field=models.BooleanField(default=False),
        ),
    ]
