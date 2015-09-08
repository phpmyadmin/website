# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_auto_20150626_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmasa',
            name='references',
            field=models.TextField(help_text=b'Links to reporter etc.', max_length=200, blank=True),
        ),
    ]
