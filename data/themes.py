# -*- coding: UTF-8 -*-
# vim: set expandtab sw=4 ts=4 sts=4:
#
# phpMyAdmin web site
#
# Copyright (C) 2008 - 2016 Michal Cihar <michal@cihar.com>
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
"""Data for themes"""


# List of theme metadata
# This is not needed for recent themes having theme.json

THEMES = {
    'aqua-2.2a': {
        'name': 'Aqua',
        'description': 'With crystal icons.',
        'author': 'Scummer',
        'supports': ['2.7', '2.8'],
    },
    'xp_dirty-1.2': {
        'name': 'WinXP - Dirty',
        'description': 'Original a clan-theme, but modified for posting here.',
        'author': 'Spockman',
        'supports': ['2.6'],
    },
    'xp_dirty-2.9a': {
        'name': 'WinXP - Dirty',
        'description': 'Original a clan-theme, but modified for posting here.',
        'author': 'Spockman',
        'supports': ['2.6', '2.7', '2.8', '2.9'],
    },
    'grid-2.11d': {
        'name': 'Grid',
        'description': '''
            Small table margins, fontsize and colors are set to be
            optimal readable and show maximum amount of data on screen.
        ''',
        'author': 'Jürgen Wind',
        'supports': ['2.8', '2.9', '3.0', '3.1', '3.2'],
    },
    'original_small-2.9': {
        'name': 'Original small',
        'description': 'Original theme altered to show a maximum amount of data.',
        'author': 'Ruben Barkow',
        'supports': ['2.9'],
    },
    'paradice-3.0a': {
        'name': 'Paradice',
        'description': 'Based on the original theme and the nuvola iconset.',
        'author': 'Andy Scherzinger, icons by David Vignoni',
        'supports': ['3.0', '3.1', '3.2', '3.3'],
    },
    'paradice-3.0b': {
        'name': 'Paradice',
        'description': 'Based on the original theme and the nuvola iconset.',
        'author': 'Andy Scherzinger, icons by David Vignoni',
        'supports': ['3.0', '3.1', '3.2', '3.3'],
    },
    'paradice-3.4': {
        'name': 'Paradice',
        'description': 'Based on the original theme and the nuvola iconset.',
        'author': 'Andy Scherzinger, icons by David Vignoni',
        'supports': ['3.4'],
    },
    'paradice-2.11e': {
        'name': 'Paradice',
        'description': 'Based on the original theme and the nuvola iconset.',
        'author': 'Andy Scherzinger, icons by David Vignoni',
        'supports': ['2.11'],
    },
    'very_small-2.9b': {
        'name': 'Very small',
        'description': 'Based on arctic ocean.',
        'author': 'Ruben Barkow; modified by Akos Szots',
        'supports': ['2.7', '2.8', '2.9'],
    },
    'very_small-2.10a': {
        'name': 'Very small',
        'description': 'Based on arctic ocean.',
        'author': 'Ruben Barkow; modified by Akos Szots',
        'supports': ['2.7', '2.8', '2.9', '2.10'],
    },
    'silk-2.10': {
        'name': 'Silk',
        'description': ''''
            "Silk" is a smooth theme designed to be clear and easy for the
            eyes, based on <a href="http://famfamfam.com/lab/icons/silk/">
            Silk icons</a> by Mark James which is licensed under the
            <a href="https://creativecommons.org/licenses/by/2.5/">
            Cc-by-2.5</a>
        ''',
        'author': 'Matthias Mailander',
        'supports': ['2.10'],
    },
    'arctic_ocean-2.11a': {
        'name': 'Arctic Ocean',
        'description': 'New theme with new database icons.',
        'author': 'Michael Keck',
        'supports': ['2.9', '2.10', '2.11'],
    },
    'arctic_ocean-3.3': {
        'name': 'Arctic Ocean',
        'description': 'New theme with new database icons.',
        'author': 'Michael Keck',
        'supports': ['3.3'],
    },
    'smooth_yellow-3.3': {
        'name': 'Smooth Yellow',
        'description': 'Based on Arctic Ocean.',
        'author': 'Michael Keck',
        'supports': ['3.3'],
    },
    'dark_lime-2.10': {
        'name': 'Dark Lime',
        'description': 'A theme with black and lime colors.',
        'author': 'GamBit',
        'supports': ['2.9', '2.10'],
    },
    'crimson_gray-2.10': {
        'name': 'Crimson Gray',
        'description': 'Theme based on Original.',
        'author': 'Audrius Kovalenko',
        'supports': ['2.9', '2.10'],
    },
    'crimson_gray-2.11b': {
        'name': 'Crimson Gray',
        'description': 'Theme based on Original.',
        'author': 'Audrius Kovalenko',
        'supports': ['2.11'],
    },
    'crimson_gray-3.1-3.2': {
        'name': 'Crimson Gray',
        'description': 'Theme based on Original.',
        'author': 'Audrius Kovalenko',
        'supports': ['3.1', '3.2'],
    },
    'pixeline-2.10': {
        'name': 'Pixeline',
        'description': 'By <a href="https://pixeline.be/">Pixeline</a>.',
        'author': 'Pixeline',
        'supports': ['2.9', '2.10'],
    },
    'pixeline-2.11a': {
        'name': 'Pixeline',
        'description': 'By <a href="https://pixeline.be/">Pixeline</a>.',
        'author': 'Pixeline',
        'supports': ['2.11'],
    },
    'hillside-2.11': {
        'name': 'Hillside',
        'description': 'Theme based on Silkline.',
        'author': 'Tim Golen',
        'supports': ['2.11'],
    },
    'hillside-3.0': {
        'name': 'Hillside',
        'description': 'Theme based on Silkline.',
        'author': 'Tim Golen',
        'supports': ['3.0', '3.1', '3.2'],
    },
    'silkline-2.11': {
        'name': 'Silkline',
        'description': 'Theme based on themes Silk and Pixeline.',
        'author': 'Douwe Ikkuh',
        'supports': ['2.11'],
    },
    'xampp-2.11': {
        'name': 'XAMPP (Apachefriends.org)',
        'description': 'This theme was built for the XAMPP-Project.',
        'author': 'Michael Keck',
        'supports': ['2.11'],
    },
    'clearview3-3.1': {
        'name': 'ClearView',
        'description': 'Very light and clear with white color and super Silk icons.',
        'author': 'beholder',
        'supports': ['3.0', '3.1', '3.2'],
    },
    'pmahomme-1.0b': {
        'name': 'pmamhomme',
        'description': 'Clean, modern and easy to use phpMyAdmin theme.',
        'author': 'Mike Homme',
        'supports': ['3.3'],
    },
    'toba-0.1': {
        'name': 'Toba',
        'description': 'Light blue theme',
        'author': 'Azhari Harahap',
        'supports': ['3.4'],
    },
    'graphite-0.9': {
        'name': 'Graphite',
        'description': 'Light grey theme using Tango icons',
        'author': 'Michal Čihař',
        'supports': ['3.4'],
    },
    'darkblue_orange-2.9': {
        'name': 'Darkblue/orange',
        'description': 'Theme included in phpMyAdmin up to 3.3',
        'author': 'Various contributors',
        'supports': ['3.4'],
    },
    'toba-0.2': {
        'name': 'Toba',
        'description': 'Light blue theme',
        'author': 'Azhari Harahap',
        'supports': ['3.4'],
    },
    'graphite-1.0': {
        'name': 'Graphite',
        'description': 'Light grey theme using Tango icons',
        'author': 'Michal Čihař',
        'supports': ['3.4'],
    },
    'darkblue_orange-2.10': {
        'name': 'Darkblue/orange',
        'description': 'Theme included in phpMyAdmin up to 3.3',
        'author': 'Various contributors',
        'supports': ['3.4'],
    },
    'darkblue_orange-2.11': {
        'name': 'Darkblue/orange',
        'description': 'Theme included in phpMyAdmin up to 3.3',
        'author': 'Various contributors',
        'supports': ['3.4'],
    },
    'blueorange-1.0b': {
        'name': 'blueorange',
        'description': 'Theme with lots of border radiuses and box shadows',
        'author': 'Teted',
        'supports': ['3.5'],
    },
    'cleanstrap-1.0': {
        'name': 'Cleanstrap',
        'description': 'Clean phpmyadmin theme with subdued colors.',
        'author': 'Various contributors',
        'supports': ['3.5'],
    },
    'metro-1.0': {
        'name': 'Metro',
        'description': 'Windows 8 Boot (Metro) theme for phpMyAdmin',
        'author': 'hplhu',
        'supports': ['3.5'],
    },
    'metro-2.0': {
        'name': 'Metro',
        'description': 'Windows 8 / Metro Theme for phpMyAdmin',
        'author': 'hplhu',
        'supports': ['3.5'],
    },
    'metro-2.1': {
        'name': 'Metro',
        'description': 'Windows 8 / Metro Theme for phpMyAdmin',
        'author': 'hplhu',
        'supports': ['3.5'],
    },
    'metro-2.2': {
        'name': 'Metro',
        'description': 'Windows 8 / Metro Theme for phpMyAdmin',
        'author': 'hplhu',
        'supports': ['4.4'],
    },
    'metro-2.3': {
        'name': 'Metro',
        'description': 'Windows 8 / Metro Theme for phpMyAdmin',
        'author': 'hplhu',
        'supports': ['4.4'],
    },
    'metro-2.4': {
        'name': 'Metro',
        'description': 'Windows 8 / Metro Theme for phpMyAdmin',
        'author': 'hplhu',
        'supports': ['4.5'],
    },
    'metro-2.5': {
        'name': 'Metro',
        'description': 'Windows 8 / Metro Theme for phpMyAdmin',
        'author': 'hplhu',
        'supports': ['4.6'],
    },
    'metro-2.6': {
        'name': 'Metro',
        'description': 'Windows 8 / Metro Theme for phpMyAdmin',
        'author': 'hplhu',
        'supports': ['4.7'],
    },
    'pmaterial-1.0': {
        'name': 'pmaterial',
        'description': 'Material Theme for phpMyAdmin',
        'author': 'jeeskdenny',
        'supports': ['4.6'],
    },
    'pmaterial-1.1': {
        'name': 'pmaterial',
        'description': 'Material Theme for phpMyAdmin',
        'author': 'jeeskdenny',
        'supports': ['4.7'],
    },
    'mhn-1.0': {
        'name': 'MHN',
        'description': 'Flat Theme for phpMyAdmin',
        'author': 'khadkamhn',
        'supports': ['4.6'],
    },
    'mhn-1.1': {
        'name': 'MHN',
        'description': 'Flat Theme for phpMyAdmin',
        'author': 'khadkamhn',
        'supports': ['4.6'],
    },
    'mhn-1.2': {
        'name': 'MHN',
        'description': 'Flat Theme for phpMyAdmin',
        'author': 'khadkamhn',
        'supports': ['4.7'],
    },
    'fallen-0.2': {
        'name': 'Fallen',
        'description': 'Fallen theme for phpMyAdmin',
        'author': 'fransallen',
        'supports': ['4.6'],
    },
    'fallen-0.3': {
        'name': 'Fallen',
        'description': 'Fallen theme for phpMyAdmin',
        'author': 'fransallen',
        'supports': ['4.6'],
    },
    'fallen-0.4': {
        'name': 'Fallen',
        'description': 'Fallen theme for phpMyAdmin',
        'author': 'fransallen',
        'supports': ['4.7'],
    },
    'fallen-0.5': {
        'name': 'Fallen',
        'description': 'Fallen theme for phpMyAdmin',
        'author': 'fransallen',
        'supports': ['4.7'],
    },
}

# List of supported phpMyAdmin versions
PMA_VERSIONS = [
    '3.0', '3.1', '3.2', '3.3', '3.4', '3.5',
    '4.4', '4.5', '4.6', '4.7', '4.8', '4.9',
    '5.0', '5.1', '5.2'
]
