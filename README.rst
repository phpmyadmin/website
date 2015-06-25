Website for phpMyAdmin
======================

Django code for phpMyAdmin's website.

Requirements
------------

Python - http://www.python.org/
    (2.7 tested)
Django - https://www.djangoproject.com/
    (1.8.2 tested)
python-feedparser - http://code.google.com/p/feedparser/
    (5.1 tested)
python-dateutil - http://labix.org/python-dateutil
    (1.5 tested)


Security announcements
----------------------

Edit announcements in the web UI.


Page generating
---------------

Each page has its own template. For most things it means inclusion of
other templates to generate full page.

Menu
----

Menu is configured in data/menu.py, the first element always means page name
second menu item title.


Themes
------

Themes require additional metadata, which is stored in data/themes.py.


Awards
------

All awards are listed in data/awards.py.


Screenshots
-----------

All screenshots are listed in data/screenshots.py.


Deployment
----------

Cron jobs:

.. code-block:: sh

    # Update translation stats
    ./manage.py fetch_translations
    # Update planet posts
    ./manage.py fetch_planet

File releases scan:

.. code-block:: sh

    # Import new releases from file storage
    ./manage.py import_files 
    # Import new themes from file storage
    ./manage.py import_themes

License
-------

The website generator is licensed under GNU GPL version 2 or later.

Website itself uses mootools <http://mootools.net/>, slimbox
<http://www.digitalia.be/software/slimbox>, fader and sorting_table
<http://madhatted.com/2008/6/20/the-joy-of-tables-on-cows> which are
licensed under terms of MIT license.

The website content is licensed under Creative Commons
Attribution-Noncommercial-Share Alike 3.0 Unported License.
