# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150624_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
