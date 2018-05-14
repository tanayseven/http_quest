.. image:: https://travis-ci.org/tanayseven/http_quiz.svg?branch=master
    :target: https://travis-ci.org/tanayseven/http_quiz
    :alt: tests

.. image:: https://coveralls.io/repos/github/tanayseven/rest-test/badge.svg?branch=HEAD
    :target: https://coveralls.io/github/tanayseven/rest-test?branch=HEAD
    :alt: test coverage

.. image:: https://api.codeclimate.com/v1/badges/15578546ce89e860fcc2/maintainability
   :target: https://codeclimate.com/github/tanayseven/rest-test/maintainability
   :alt: Maintainability

.. image:: https://img.shields.io/github/license/tanayseven/rest-test.svg
    :target: https://github.com/tanayseven/rest-test/blob/master/LICENSE.txt
    :alt: license

.. image:: https://img.shields.io/github/repo-size/tanayseven/rest-test.svg
    :target: https://travis-ci.org/tanayseven/http_quiz
    :alt: GitHub repo size in bytes


HTTP Quiz
=========

Have your own quiz over HTTP
----------------------------

A modular platform that helps you add your custom Quiz or let's you make one of your candidate to have


Architecture
============

Files and directories in root
-----------------------------

1. ``http_quiz`` contains the main source code which is the production code that runs this application. These are
   further divided into modules, each module handling some responsibility in the system. Checkout the subsection
   modules_.
2. ``migrations`` contains the database migration files right from the very first migration to the latest one. use the
   command ``flask db --help`` to know how to use migrations.
3. ``test`` contains the source code which tests the production code. Most of the tests written in the ``test``
   directory are HTTP api level tests.
4. ``create_test_database`` creates test database in the postgres container. This will be helpful for creating a test
   database after just starting a container esp. if you change the schema of the database and need to flush the existing
   test database.
5. ``app_exec`` is used to execute a command inside the app container from the outside. The app container is the
   container that runs the flask web app.
6. ``db_exec`` is used to execute a command inside the database container from the outside. The database container is
   the container that runs postgres.
7. ``reset_ownership`` (for linux) is used for resetting the permissions of the files that are generated/created from
   inside the containers in the shared volume. They are by default owned by root on creation.

.. _modules:

Modules
-------

The project consists of modules which is further divided into different files.

1. ``model.py`` contains all the models needed by the module in which this is placed. The models in this place.
2. ``repo.py`` contains the data manipulation functionality abstracting out the handling of database sessions. It also
   uses different models of various different modules.
3. ``translations.py`` contains localized translation for all the strings used throughout the project.
4. ``schema.py`` contains json schema that is used to validate JSON entering an HTTP endpoint
5. ``view.py`` contains definition of an HTTP endpoint which can either be a GET or a POST
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

To build all the Docker images using ``docker-compose``

.. code-block:: bash

    docker-compose build

To run the whole application as containers using ``docker-compose``

.. code-block:: bash

    docker-compose up


To run all the tests in the application run

.. code-block:: bash

    ./app_exec pytest # Just run the tests
    ./app_exec pytest --cov http_quiz test/ # Run tests with coverage

To perform migrations run

.. code-block:: bash

    ./app_exec flask db migrate # Detect and create migration files
    ./app_exec flask db upgrade # Actually perform migrations on the database
    ./app_exec flask db --help # For info about the other database migration commands


For Linux only: files created by a container (like migration files) are owned by root because Docker runs as root

.. code-block:: bash

    ./reset_ownership # needs sudo password, will change the owner to yourself

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
