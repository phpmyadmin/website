Website for phpMyAdmin
======================

Django code for phpMyAdmin's website.

.. image:: https://travis-ci.org/phpmyadmin/website.svg?branch=master
    :target: https://travis-ci.org/phpmyadmin/website

.. image:: https://codecov.io/github/phpmyadmin/website/coverage.svg?branch=master
    :target: https://codecov.io/github/phpmyadmin/website?branch=master

.. image:: https://api.codacy.com/project/badge/Grade/4cfc116f766947dcad6c006b295aafc2    
    :target: https://www.codacy.com/app/phpMyAdmin/website

Requirements
------------

Website needs Python 2.7, additional dependencies are listed in `requirements.txt`.


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

You will need to apply migrations before loading test data:

.. code-block:: sh

    ./manage.py migrate

You might want to import some data to have at least some content on the website:

.. code-block:: sh

    ./manage.py loaddata pmaweb/fixtures/test_data.json

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

Website itself uses some MIT licensed Javascript libraries:

* jQuery <https://jquery.com/>
* Bootstrap <https://getbootstrap.com/>
* Colorbox <https://www.jacklmoore.com/colorbox/>

The website content is licensed under Creative Commons
Attribution-Noncommercial-Share Alike 3.0 Unported License.
