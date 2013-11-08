![Build status](https://secure.travis-ci.org/sycy600/todoer.png?branch=master)

Write what you have done and what you want to do.

How to setup
============

Get ``buildout``::

    python2.7 bootstrap.py

Create project structure::

    bin/buildout

Run application (application is accessible at [http://localhost:5000](http://localhost:5000))::

    bin/todoer

Testing
=======

Tests are placed in directory ``src/todoer/tests``.

The pattern for test filename is ``*_tests.py``.

Run only tests::

    bin/test

Run tests, check flake8::

    bin/check
