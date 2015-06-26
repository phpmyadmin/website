# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('translated', models.IntegerField()),
                ('percent', models.DecimalField(max_digits=4, decimal_places=1)),
                ('updated', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
