# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=50)),
                ('md5', models.CharField(max_length=32)),
                ('sha1', models.CharField(max_length=40)),
                ('signed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=50)),
                ('release_notes', models.TextField()),
                ('featured', models.BooleanField()),
                ('visible', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='download',
            name='release',
            field=models.ForeignKey(to='files.Release'),
        ),
    ]
