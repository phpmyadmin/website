# -*- coding: UTF-8 -*-
# phpMyAdmin web site generator
#  - data for awards
#
# Copyright (C) 2008 Michal Cihar <michal@cihar.com>
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

# List of awards
AWARDS = [
    {
        'image': 'percona-live-logo.png',
        'link': 'http://openlife.cc/blogs/2013/april/mysql-community-awards-2013-and-winners-are',
        'title': '2013 MySQL Community Awards',
        'text': '''
<p>At the <a href="%(link)s">2013 MySQL Community Awards</a> ceremony, our
project has won</p>
<p class="award">MySQL Application of the year 2013</p>
    ''',
        'photos': [
            (
                '2013-community-awards-1.jpg',
                'The trophy',
                'The trophy'
            ),
            (
                '2013-community-awards-2.jpg',
                'The trophy detail',
                'The trophy detail'
            ),
        ],
    },
    {
        'image': 'sf_cca_2009_logo.png',
        'link': 'http://sourceforge.net/community/cca09',
        'title': '2009 SourceForge.net Community Choice Awards',
        'text': '''
<p>For the <a href="%(link)s">2009 SourceForge.net Community Choice Awards</a>,
phpMyAdmin was present in two categories:</p>
<p class="award">Best Tool or Utility for Developers (finalist)</p>
<p class="award">Best Tool or Utility for SysAdmins (winner)</p>
    ''',
        'photos': [('sf_cca_2009_trophy.jpg', 'The trophy', 'The trophy')],
    },
    {
        'image': 'infoworld-bossie-2008.jpg',
        'link': 'http://www.infoworld.com/slideshow/2008/08/171-best_of_open_so-5.html',
        'title': 'InfoWorld 2008 Best of Open Source Awards',
        'text': '''
<p>Our project has won this <a href="%(link)s">Infoworld 2008 award:</a></p>
<p class="award">Best of open source platforms and middleware
(MySQL administration)</p>
    ''',
        'photos': [],
    },
    {
        'image': 'sf_cca_2008_winner.png',
        'link': 'http://sourceforge.net/community/index.php/landing-pages/cca08',
        'title': '2008 SourceForge.net Community Choice Awards',
        'text': '''
<p>For the <a href="%(link)s">2008 SourceForge.net Community Choice Awards</a>,
phpMyAdmin was present in three categories:</p>
<p class="award">Best Tool or Utility for Developers (finalist)</p>
<p class="award">Best Tool or Utility for SysAdmins (winner)</p>
<p class="award">Most Likely to Be the Next $1B Acquisition (winner)</p>
    ''',
        'photos': [
            (
                'sf_cca_2008_trophies.jpg',
                'The two trophies',
                'The two trophies'
            )
        ],
    },
    {
        'image': 'sf_cca_2007_sysadmin.gif',
        'link': 'http://sourceforge.net/community/index.php/landing-pages/cca07',
        'title': '2007 SourceForge.net Community Choice Awards',
        'text': '''
<p>For the <a href="%(link)s">2007 SourceForge.net Community Choice Awards</a>,
phpMyAdmin was present in two categories:</p>
<p class="award">Best Tool or Utility for Developers (nominated)</p>
<p class="award">Best Tool or Utility for SysAdmins (winner)</p>
    ''',
        'photos': [('sf_cca_2007_trophy.jpg', 'The trophy', 'The trophy')],
    },
    {
        'image': '2006-trophees-logo.png',
        'link': 'http://www.tropheesdulibre.org/',
        'title': '2006 Trophees du Libre',
        'text': '''
<p>phpMyAdmin has won a Silver Trophy at the Third
<a href="%(link)s">Trophees du Libre</a> (Free Software Awards)
in the category</p>
<p class="award">PHP</p>
    ''',
        'photos': [
            (
                '2006-trophees-marc.jpg',
                'Receiving the award',
                'Marc Delisle (right) receiving the award in the name of '
                'the phpMyAdmin development team.'
            )
        ],
    },
    {
        'image': '2005-os2world.png',
        'link': 'http://www.os2world.com/cgi-bin/news/viewnews.cgi?category=29&id=1145794857',
        'title': '2005 OS2World.com Awards',
        'text': '''
<p>For the <a href="%(link)s">5th Annual OS/2 World Awards</a>,
phpMyAdmin won in the category</p>
<p class="award">Best PHP Application</p>
    ''',
        'photos': [],
    },
    {
        'image': 'sf_cca_2006_winner.png',
        'link': 'http://sourceforge.net/community/index.php/cca06',
        'title': '2006 SourceForge.net Community Choice Awards',
        'text': '''
<p>For the first annual SourceForge.net <a href="%(link)s">Community Choice
Awards</a>, phpMyAdmin won the first place in two categories:</p>
<p class="award">Databases</p>
<p class="award">Sysadmin</p>
    ''',
        'photos': [],
    },
    {
        'image': '2006-phpmag-ger.png',
        'link': 'http://www.phpmagazin.de/itr/service/psecom,id,304,nodeid,64.html',
        'title': 'PHP Magazin Reader\'s Choice Award 2006',
        'text': '''
<p>phpMyAdmin was awarded the Reader's Choice Award 2006 in the category</p>
<p class="award">Best PHP-Tool / Best PHP-Application</p>
<p>by the readers of the <a href="%(link)s">German PHP Magazin</a>.</p>
    ''',
        'photos': [],
    },
    {
        'image': '2005-phpmag-ger.gif',
        'link': 'http://www.phpmagazin.de/umfrage2005',
        'title': 'PHP Magazin Reader\'s Choice Award 2005',
        'text': '''
<p>phpMyAdmin was awarded the Reader's Choice Award 2005 in the category</p>
<p class="award">Best PHP-Tool / Best PHP-Application</p>
<p>by the readers of the <a href="%(link)s">German PHP Magazin</a>.</p>
    ''',
        'photos': [],
    },
    {
        'image': '2003-phpmag-ger.gif',
        'link': 'http://www.php-mag.de/itr/service/show.php3?id=109&nodeid=64',
        'title': 'PHP Magazin Reader\'s Choice Award 2003',
        'text': '''
<p>phpMyAdmin was awarded the Reader's Choice Award 2003 in the category</p>
<p class="award">Best PHP-Tool / Best PHP-Application</p>
<p>by the readers of the <a href="%(link)s">German PHP Magazin</a>.</p>
    ''',
        'photos': [
            (
                '2003-php-conf.jpg',
                'Receiving the award',
                'Alexander Turek and Garvin Hicking receiving the award '
                'in the name of the phpMyAdmin development team at '
                '2003 PHP International Conference.'
            )
        ],
    },
    {
        'image': '2003-phpmag-int.gif',
        'link': 'http://www.php-mag.de/itr/service/show.php3?id=109&nodeid=64',
        'title': 'International PHP Magazine Reader\'s Choice Award 2003',
        'text': '''
<p>phpMyAdmin was awarded the Reader's Choice Award 2003 in the category</p>
<p class="award">Best PHP-Tool / Best PHP-Application</p>
<p>by the readers of the <a href="%(link)s">International PHP Magazine</a>.</p>
    ''',
        'photos': [
            (
                '2003-php-conf.jpg',
                'Receiving the award',
                'Alexander Turek and Garvin Hicking receiving the award '
                'in the name of the phpMyAdmin development team at '
                '2003 PHP International Conference.'
            )
        ],
    },
    {
        'image': '2002-12-sfnet-potm.png',
        'link': 'http://sourceforge.net/potm/potm-2002-12.php',
        'title': 'Sourceforge.net project of the month',
        'text': '''
<p>phpMyAdmin was awarded
<a href="http://sourceforge.net">Sourceforge.net</a>'s</p>
<p class="award"><a href="%(link)s">Project of the month</a></p>
<p>in December 2002. Have a look at that <a href="%(link)s">article</a>, if you
want to learn about the early years of phpMyAdmin.</p>
    ''',
        'photos': [],
    },
]

# Allow award text to use other things as format string
from cgi import escape
for award in AWARDS:
    award['text'] = award['text'] % {
        'link': escape(award['link'])
    }
