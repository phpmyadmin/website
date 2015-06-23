# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pmasa',
            options={'ordering': ('year', 'sequence')},
        ),
        migrations.AlterField(
            model_name='pmasa',
            name='updated',
            field=models.DateField(help_text=b'Set this in case of major update to the entry', null=True, blank=True),
        ),
    ]
