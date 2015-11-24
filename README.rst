Website for phpMyAdmin
======================

Django code for phpMyAdmin's website.

.. image:: https://travis-ci.org/phpmyadmin/website.svg?branch=master
    :target: https://travis-ci.org/phpmyadmin/website

.. image:: http://codecov.io/github/phpmyadmin/website/coverage.svg?branch=master
    :target: http://codecov.io/github/phpmyadmin/website?branch=master

.. image:: https://api.codacy.com/project/badge/4cfc116f766947dcad6c006b295aafc2
    :alt: Codacy Badge
    :target: https://www.codacy.com/app/nijel/phpmyadmin-website

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


Security announcements and news
-------------------------------

Edit announcements and news entries in the web UI.

Security issues are not publicly visible as long as they are marked as draft.
The are accessible through separate URL (you can click `View on the site` link
while editing).


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


Development
-----------

For development, first install dependencies. The ones needed for running the
server are listed in ``requirements.txt``, for running testsuite in
``requirements-test.txt``. You can install them using your distribution (the
package names will usually add python- prefix) or using pip:

.. code-block:: sh

    pip install -r requirements-test.txt

Once you have all dependencies, you can start development server:

.. code-block:: sh

    ./manage.py runserver

It will listed on port 8080 by default (you can change this by parameters).

To run testuite execute:

.. code-block:: sh

    ./manage.py test


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
