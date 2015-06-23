# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_auto_20150623_0931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pmasa',
            options={'ordering': ('year', 'sequence'), 'verbose_name': 'PMASA', 'verbose_name_plural': 'PMASAs'},
        ),
        migrations.AddField(
            model_name='pmasa',
            name='draft',
            field=models.BooleanField(default=True, help_text=b'Draft entries are not shown in website listings'),
        ),
    ]
