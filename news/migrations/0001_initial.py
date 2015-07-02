# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique_for_date=b'date')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('body', markupfield.fields.MarkupField(rendered_field=True)),
                ('body_markup_type', models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown'), (b'restructuredtext', 'Restructured Text')])),
                ('_body_rendered', models.TextField(editable=False)),
                ('author', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
