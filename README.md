![Build status](https://secure.travis-ci.org/sycy600/todoer.png?branch=master)

Write what you have done and what you want to do.

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

Run tests, check flake8 (pep8 and complexity):

    bin/check
