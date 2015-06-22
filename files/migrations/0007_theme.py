# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0006_auto_20150622_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('version', models.CharField(unique=True, max_length=50)),
                ('filename', models.FilePathField(path=b'/home/mcihar/work/phpmyadmin/website/frs/themes', recursive=True, match=b'.*\\.zip$')),
                ('supported_versions', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
