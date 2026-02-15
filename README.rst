Website for phpMyAdmin
======================

Django code for phpMyAdmin's website.

.. image:: https://github.com/phpmyadmin/website/actions/workflows/tests.yml/badge.svg?branch=master
    :alt: Tests
    :target: https://github.com/phpmyadmin/website/actions/workflows/tests.yml?query=branch%3Amaster

.. image:: https://codecov.io/github/phpmyadmin/website/coverage.svg?branch=master
    :target: https://codecov.io/github/phpmyadmin/website?branch=master

Requirements
------------

Website needs Python 3.13, additional dependencies are listed in `requirements.txt`.


Security announcements and news
-------------------------------

Edit announcements and news entries in the web UI.

Security issues are not publicly visible as long as they are marked as draft.
They are accessible through a separate URL (you can click `View on the site` link
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
server are listed in ``requirements.txt`` and the ones for running the testsuite are in
``requirements-test.txt``.

You can install them using pip or using packages from your distribution
(see `Debian packages`_)
to avoid to have to use ``--break-system-packages``.

.. code-block:: sh

    pip install -r requirements-test.txt

You will need to apply migrations before loading test data:

.. code-block:: sh

    ./manage.py migrate

You might want to import some data to have at least some content on the website:

.. code-block:: sh

    ./manage.py loaddata pmaweb/fixtures/test_data.json

Once you have all dependencies, you can start the development server:

.. code-block:: sh

    ./manage.py runserver

It will listen on port 8000 by default (or use: `./manage.py runserver 127.0.0.1:8080` for a different port).

To run the test-suite execute:

.. code-block:: sh

    ./manage.py test

To add a new user (for `/admin/`):

.. code-block:: sh

    ./manage.py createsuperuser

Deployment
----------

On a Debian Trixie server:

.. _Debian packages:

.. code-block:: sh

    # Install Python pip
    apt install -y \
    python3-django \
    python3-dateutil \
    python3-feedparser \
    python3-django-markupfield \
    python3-docutils \
    python3-markdown \
    python3-pytz \
    python3-bs4 \
    python3-django-compressor \
    python3-django-appconf \
    python3-mysqldb

You might need to ensure the `PYTHONPATH` ENV variable is set to the correct value.
Or commands will output ``ModuleNotFoundError: No module named 'django'`` or something very similar.

.. code-block:: sh
    # Define the PYTHONPATH variable
    # Maybe add this to your ~/.bashrc ?
    export PYTHONPATH="/usr/local/lib/python3.13/site-packages/:/usr/lib/python3/dist-packages/:${PYTHONPATH}"

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

* `jQuery <https://jquery.com/>`_
* `Bootstrap <https://getbootstrap.com/>`_
* `Colorbox <https://www.jacklmoore.com/colorbox/>`_

The website content is licensed under Creative Commons
Attribution-Noncommercial-Share Alike 3.0 Unported License.
