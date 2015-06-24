# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0016_auto_20150624_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='_release_notes_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='release',
            name='release_notes_markup_type',
            field=models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown'), (b'restructuredtext', 'Restructured Text')]),
        ),
        migrations.AlterField(
            model_name='release',
            name='release_notes',
            field=markupfield.fields.MarkupField(rendered_field=True),
        ),
    ]
