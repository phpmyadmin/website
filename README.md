Website generator for phpMyAdmin
================================

This is currently in alpha state, but later it will hopefully replace
phpMyAdmin homepage.


Requirements
------------

Python - http://www.python.org/
    (2.7 tested, other should work also)
Genshi -  http://genshi.edgewall.org/
    (0.6.0 tested)
python-feedparser - http://code.google.com/p/feedparser/
    (5.1 tested)
python-dateutil - http://labix.org/python-dateutil
    (1.5 tested)


Security announcements
----------------------

To create a new security announcement, copy templates/security/_PMASA_ to
templates/security/PMASA-YYYY-N and edit its contents.


Page generating
---------------

Each page has its own template. For most things it means inclusion of
other templates to generate full page. These partial includes should be
named with underscore as first character (eg. _page.tpl).

To add a new page, simply put a file named something.tpl to the templates 
directory and it will be automatically used as a template on next run.

All pages should at the end include _page.tpl to get layout and other
common things. You can see example page at templates/_sample_.tpl

Static data required for generating pages is stored in data/ folder.

Menu
----

Menu is configured in data/menu.py, the first element always means page name
(extension is added automatically) second menu item title.


Themes
------

Themes require additional metadata, which is stored in data/themes.py.


Awards
------

All awards are listed in data/awards.py.


Screenshots
-----------

All screenshots are listed in data/screenshots.py.


Markup rules
------------

(See genshi docs for more details).

- $ is special char to indicate template variable, to escape it, use $$
- comments which first char is ! (eg. <!--! comment -->) will not be in output


Special pages
-------------

Directory static contains some special pages, which have to be present
on the website. First there is version.php script, which shows most
current phpMyAdmin version, which is then offered as an update. The rest
are currently just compatibility files with old website - security.php,
which redirects security issues to new pages and _redirect.tpl which is
used for generating redirects based on data/redirects.py.


Generating website
------------------

The website itself is rendered using render.py, here are options which
are currently used for http://www.phpmyadmin.net/home_page/::

    ./render.py \
        --quiet \
        --server http://www.phpmyadmin.net \
        --base-url /home_page/ \
        --quiet-cache \
        --log render.log \
        --extension php

If you want to make log visible on website, copy it to output folder::

    cp render.log output/

And finally rsync it to sourceforge::

    rsync -az --delete output/ user,phpmyadmin@web.sourceforge.net:htdocs/home_page/

Automatic build
---------------

There is configured automatic build of website, which runs every hour.
In case website is not updated, you might want to check the build log
for any possible failures:

http://www.phpmyadmin.net/home_page/render.log

Twitter integration
-------------------

The script can post new security issues and news to Twitter. You need to have
tweepy module for that and configure Twitter credentials in `~/.pmaweb`::

    [twitter]
    consumer_key = <consumer key>
    consumer_secret = <consumer secret>
    token_key = <access token key>
    token_secret = <access token secret>

Information about obtaining these OAuth tokens is available at 
http://pythonhosted.org/tweepy/html/auth_tutorial.html.

License
-------

The website generator is licensed under GNU GPL version 2 or later.

Website itself uses mootools <http://mootools.net/>, slimbox
<http://www.digitalia.be/software/slimbox>, fader and sorting_table
<http://madhatted.com/2008/6/20/the-joy-of-tables-on-cows> which are
licensed under terms of MIT license.

The website content is licensed under Creative Commons
Attribution-Noncommercial-Share Alike 3.0 Unported License.
