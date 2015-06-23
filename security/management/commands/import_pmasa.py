# -*- coding: UTF-8 -*-
# vim: set expandtab sw=4 ts=4 sts=4:
#
# phpMyAdmin web site
#
# Copyright (C) 2008 - 2015 Michal Cihar <michal@cihar.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
from django.core.management.base import BaseCommand
from django.conf import settings
import os
from xml.etree import ElementTree
from htmlentitydefs import name2codepoint
from dateutil import parser
from security.models import PMASA

INTRO = """<?xml version="1.0"?>
<!DOCTYPE data PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
"""


class EntityDict(object):
    def __getitem__(self, item):
        return unichr(name2codepoint[item])


class PMASAParser(object):
    simple_items = (
        'summary', 'severity', 'mitigation', 'affected', 'solution', 'cve', 'cwe',
        'references', 'unaffected',
    )
    def __init__(self):
        self.data = {'commits': '', 'draft': False}
        self.commits = {}

    def parse(self, item, text):
        prefix, suffix = item.split('_', 1)
        assert prefix == 'announcement'
        if suffix in self.simple_items:
            self.data[suffix] = text
        elif suffix.startswith('commits'):
            if '_' in suffix:
                self.parse_announcement_commits(text, suffix.split('_', 1)[1])
            else:
                self.parse_announcement_commits(text, 'master')
        else:
            getattr(self, 'parse_{0}'.format(item))(text)

    def parse_announcement_id(self, text):
        prefix, year, sequence = text.split('-')
        assert prefix == 'PMASA'
        self.data['year'] = int(year)
        self.data['sequence'] = int(sequence)

    def parse_announcement_date(self, text):
        self.data['date'] = parser.parse(text).date()

    def parse_announcement_updated(self, text):
        if ' ' in text:
            print 'Skipping second part:', text
        text = text.split()[0]
        self.data['updated'] = parser.parse(text).date()

    def parse_announcement_description(self, text):
        self.data['description'] = u'<p>{0}</p>'.format(text)
        self.data['description_markup_type'] = 'html'

    def parse_announcement_description_fmt(self, text):
        self.data['description'] = text
        self.data['description_markup_type'] = 'html'

    def parse_announcement_commits(self, text, branch):
        self.commits[branch.replace('_', '.')] = text.replace('\n', ' ')
        result = []
        if 'master' in self.commits:
            result.append(self.commits['master'])
        for branch in sorted(self.commits):
            if branch == 'master':
                continue
            result.append('{0}: {1}'.format(branch, self.commits[branch]))

        self.data['commits'] = '\n'.join(result)


class Command(BaseCommand):
    help = 'Imports PMASA entries from filesystem'


    def process_entry(self, path, name):
        parser = ElementTree.XMLParser()
        parser.entity = EntityDict()
        filename = os.path.join(path, name)
        with open(filename, 'r') as handle:
            data = handle.read()

        print name

        tree = ElementTree.fromstring(INTRO + data, parser)

        result = PMASAParser()

        for item in tree.findall('{http://genshi.edgewall.org/}def'):
            text = ElementTree.tostring(item)
            text = text.split(">", 1)[1].rsplit("<", 1)[0].strip()
            result.parse(item.get('function'), text)

        PMASA.objects.get_or_create(
            year=result.data['year'],
            sequence=result.data['sequence'],
            defaults=result.data
        )


    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'pmaweb', 'templates', 'security')
        for filename in os.listdir(path):
            if not filename.startswith('PMASA-'):
                continue
            self.process_entry(path, filename)
