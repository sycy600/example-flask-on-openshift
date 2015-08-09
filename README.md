An example of Flask application with setup of Buildout and unit tests which can be automatically deployed to OpenShift

How to setup
============

Python versions supported: `2.7`, `3.3`.

Get ``buildout``:

    python bootstrap.py

Create project structure:

    bin/buildout

Run application (application is accessible at [http://localhost:5000](http://localhost:5000)):

    bin/todoer

Testing
=======

Tests are placed in directory ``src/todoer/tests``.

The pattern for test filename is ``*_tests.py``.

Run only tests and check coverage:

    bin/test

Run tests, check flake8 (pep8 and cyclomatic complexity):

    bin/check

Deployment
==========

Deployment is automatically performed by Travis using info in ``.travis.yml`` file. WSGI entry point object which is used by OpenShift resides in file ``wsgi/application`` and is named ``application``.
