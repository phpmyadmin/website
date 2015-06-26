# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20150622_0920'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='download',
            unique_together=set([('release', 'filename')]),
        ),
    ]
