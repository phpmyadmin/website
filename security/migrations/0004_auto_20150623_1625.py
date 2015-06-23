# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0003_auto_20150623_0933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pmasa',
            options={'ordering': ('-year', '-sequence'), 'verbose_name': 'PMASA', 'verbose_name_plural': 'PMASAs'},
        ),
        migrations.AlterField(
            model_name='pmasa',
            name='affected',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pmasa',
            name='mitigation',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pmasa',
            name='references',
            field=models.TextField(help_text=b'Links to reporter etc.', max_length=200),
        ),
        migrations.AlterField(
            model_name='pmasa',
            name='solution',
            field=models.TextField(default=b'Upgrade to phpMyAdmin ? or newer or apply patch listed below.', max_length=200),
        ),
        migrations.AlterField(
            model_name='pmasa',
            name='unaffected',
            field=models.TextField(blank=True),
        ),
    ]
