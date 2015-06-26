# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=50)),
                ('size', models.IntegerField(default=0)),
                ('md5', models.CharField(max_length=32)),
                ('sha1', models.CharField(max_length=40)),
                ('signed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-release__version_num', 'filename'],
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(unique=True, max_length=50)),
                ('version_num', models.IntegerField(default=0, unique=True)),
                ('release_notes', markupfield.fields.MarkupField(rendered_field=True)),
                ('stable', models.BooleanField(default=False, db_index=True)),
                ('release_notes_markup_type', models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown'), (b'restructuredtext', 'Restructured Text')])),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('_release_notes_rendered', models.TextField(editable=False)),
            ],
            options={
                'ordering': ['-version_num'],
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('display_name', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('filename', models.CharField(unique=True, max_length=100)),
                ('supported_versions', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('size', models.IntegerField(default=0)),
                ('md5', models.CharField(max_length=32)),
                ('sha1', models.CharField(max_length=40)),
                ('signed', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
            ],
            options={
                'ordering': ['name', 'version'],
            },
        ),
        migrations.AddField(
            model_name='download',
            name='release',
            field=models.ForeignKey(to='files.Release'),
        ),
        migrations.AlterUniqueTogether(
            name='download',
            unique_together=set([('release', 'filename')]),
        ),
    ]
