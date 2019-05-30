Python bindings for Pinocchio C++ library
=========================================

.. image:: https://travis-ci.org/alexanderlarin/pynocchio.svg?branch=master
    :target: https://travis-ci.org/alexanderlarin/pynocchio


Based on:

* amazing paper `"Automatic Rigging and Animation of 3D Characters," SIGGRAPH 2007 <http://people.csail.mit.edu/ibaran/papers/2007-SIGGRAPH-Pinocchio.pdf>`_
* Pinocchio C++ library sources (`github repository <https://github.com/elrond79/Pinocchio>`_)

Supported platforms:

* Windows
* Linux
* OSX (in progress)

Prerequisites
-------------
On Unix (Linux, OS X)

* A compiler with C++11 support
* CMake >= 2.8.12

On Windows

* Visual Studio 2015 (required for all Python versions, see notes below)
* CMake >= 3.1

Installation
------------

Install **pynocchio** with pip:

.. code-block::

    pip install pynocchio

Examples
--------

We provide some basic examples on how to use **pynocchio** in Python in the `examples <https://github.com/alexanderlarin/pynocchio/tree/master/examples>`_ directory.
