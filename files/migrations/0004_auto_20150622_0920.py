# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_auto_20150622_0908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='download',
            options={'ordering': ['filename']},
        ),
        migrations.AddField(
            model_name='download',
            name='size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
