.. image:: https://travis-ci.org/tanayseven/http_quest.svg?branch=master
    :target: https://travis-ci.org/tanayseven/http_quest
    :alt: tests

.. image:: https://coveralls.io/repos/github/tanayseven/http_quest/badge.svg?branch=HEAD
    :target: https://coveralls.io/github/tanayseven/http_quest?branch=HEAD
    :alt: test coverage

.. image:: https://api.codeclimate.com/v1/badges/a939e0acceece8e12b6b/maintainability
   :target: https://codeclimate.com/github/tanayseven/http_quest/maintainability
   :alt: Maintainability

.. image:: https://img.shields.io/github/license/tanayseven/http_quest.svg?cacheSeconds=86400
    :target: https://github.com/tanayseven/http_quest/blob/master/LICENSE.txt
    :alt: license

.. image:: https://img.shields.io/github/repo-size/tanayseven/http_quest.svg?cacheSeconds=86400
    :target: https://travis-ci.org/tanayseven/http_quest
    :alt: GitHub repo size in bytes


HTTP Quest
==========

Have your own quest over HTTP
-----------------------------

A modular platform that helps you add your custom quest for your users to solve in by writing programs that communicate
with this application via HTTP


Architecture
============

Files and directories in root
-----------------------------

1. ``http_quest`` contains the main source code which is the production code that runs this application. These are
   further divided into modules, each module handling some responsibility in the system. Checkout the subsection
   modules_.
2. ``migrations`` contains the database migration files right from the very first migration to the latest one. use the
   command ``flask db --help`` to know how to use migrations.
3. ``test`` contains the source code which tests the production code. Most of the tests written in the ``test``
   directory are HTTP api level tests.

.. _modules:

Modules
-------

The project consists of modules which are further divided into different files.

1. ``model.py`` contains all the models needed by the module in which this is placed. The models in this place.
2. ``repo.py`` contains the data manipulation functionality abstracting out the handling of database sessions. It also
   uses different models of various different modules.
3. ``translations.py`` contains a localised translation for all the strings used throughout the project.
4. ``schema.py`` contains JSON schema that is used to validate JSON entering an HTTP endpoint
5. ``view.py`` contains definitions of HTTP endpoints which can either be GET or POST or any other ones
6. ``<business_logic>.py`` something like for example ``user.py`` which will contain all the business logic for that
   sub-domain, in this example it will contain business logic for the user sub-domain.

Setting up and using
====================

Prerequisites
-------------

* Docker
* Docker Compose

Usage Instructions
~~~~~~~~~~~~~~~~~~

The project is developed/build using poetry and you need it installed to proceed

To install all the packages in a newly created virtual environment from the lock file:

.. code-block:: bash

    poetry install

To run the project (make sure that your database is setup):

.. code-block:: bash

    poetry run flask run

To run all the tests run:

.. code-block:: bash

    poetry run pytest
    poetry run pytest test/unit # just run the unit tests
    poetry run pytest -k test_name_of_the_test_case # just run one test case

Run all tests with code coverage and check it on browser

.. code-block:: bash

    poetry run pytest --cov-report=html --cov=http_quest --cov=test test/ # Run tests with coverage
    cd htmlcov # the directory where coverage report is generated
    poetry run python -m http.server # run an http server to browse the report

To perform migrations run

.. code-block:: bash

    poetry run flask db migrate # Detect and create migration files
    poetry run flask db upgrade # Actually perform migrations on the database
    poetry run flask db --help # For info about the other database migration commands

To extract translations used in the code into a pot file (when new strings are added in .py files):

.. code-block:: bash

    poetry run pybabel extract -F babel.cfg -o messages.pot .

To create translations for the extracted pot file into a po file (then manually add the translations to the new po file):

.. code-block:: bash

    pybabel update -i messages.pot -d translations


LICENSE
=======

The MIT License (MIT)

Copyright (c) 2018 Tanay PrabhuDesai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
