# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0008_auto_20150622_0956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'ordering': ['name', 'version']},
        ),
    ]
