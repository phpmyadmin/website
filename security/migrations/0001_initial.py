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
            name='PMASA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=2015, choices=[(2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)])),
                ('sequence', models.IntegerField(help_text=b'Sequence number of PMASA in given year')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('updated', models.DateTimeField(help_text=b'Set this in case of major update to the entry', null=True, blank=True)),
                ('summary', models.CharField(max_length=200)),
                ('description', markupfield.fields.MarkupField(rendered_field=True)),
                ('severity', models.CharField(max_length=200)),
                ('description_markup_type', models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown'), (b'restructuredtext', 'Restructured Text')])),
                ('mitigation', models.TextField(blank=True)),
                ('_description_rendered', models.TextField(editable=False)),
                ('affected', models.TextField()),
                ('unaffected', models.TextField(blank=True)),
                ('solution', models.TextField(default=b'Upgrade to phpMyAdmin ? or newer or apply patch listed below.', max_length=200)),
                ('references', models.TextField(help_text=b'Links to reporter etc.', max_length=200)),
                ('cve', models.CharField(help_text=b'Space separated list of related CVE entries', max_length=200)),
                ('cwe', models.CharField(default=b'661', help_text=b'Space separated list of CWE classifications', max_length=200)),
                ('commits', models.TextField(help_text=b'Space separated list of commits, commits for different branches should be placed on separate line prefixed with version prefix. For example: 3.5: 01d35b3558e47fba947719857bd71f6fd9e5dce8')),
                ('draft', models.BooleanField(default=True, help_text=b'Draft entries are not shown in website listings')),
            ],
            options={
                'ordering': ('-year', '-sequence'),
                'verbose_name': 'PMASA',
                'verbose_name_plural': 'PMASAs',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pmasa',
            unique_together=set([('year', 'sequence')]),
        ),
    ]
