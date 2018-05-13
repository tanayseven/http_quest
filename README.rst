.. image:: https://travis-ci.org/tanayseven/rest-test.svg?branch=master
    :alt: tests
    :target: https://travis-ci.org/tanayseven/rest-test

.. image:: https://coveralls.io/repos/github/tanayseven/rest-test/badge.svg?branch=HEAD
    :alt: test coverage
    :target: https://coveralls.io/github/tanayseven/rest-test?branch=HEAD

.. image:: https://api.codeclimate.com/v1/badges/15578546ce89e860fcc2/maintainability
   :target: https://codeclimate.com/github/tanayseven/rest-test/maintainability
   :alt: Maintainability

.. image:: https://img.shields.io/github/license/tanayseven/rest-test.svg
    :alt: license
    :target: https://github.com/tanayseven/rest-test/blob/master/LICENSE.txt

.. image:: https://img.shields.io/github/repo-size/tanayseven/rest-test.svg
    :alt: GitHub repo size in bytes


HTTP Quiz
=========


Have your own quiz over HTTP
----------------------------

A modular platform that helps you add your custom Quiz


Prerequisites
~~~~~~~~~~~~~

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


For Linux only: files created by container (like migration files) are owned by root because Docker runs as root

.. code-block:: bash

    ./reset_ownership # needs sudo password, will change the owner to yourself
