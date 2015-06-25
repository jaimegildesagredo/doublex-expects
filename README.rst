===============
Doublex Expects
===============

.. image:: https://img.shields.io/pypi/v/doublex-expects.svg
    :target: https://pypi.python.org/pypi/doublex-expects
    :alt: Latest version

.. image:: https://img.shields.io/badge/Licence-Apache2-brightgreen.svg
    :target: https://www.tldrlegal.com/l/apache2
    :alt: License

.. image:: https://img.shields.io/pypi/dm/doublex-expects.svg
    :target: https://pypi.python.org/pypi/doublex-expects
    :alt: Number of PyPI downloads

.. image:: https://secure.travis-ci.org/jaimegildesagredo/doublex-expects.svg?branch=master
    :target: http://travis-ci.org/jaimegildesagredo/doublex-expects

Doublex-Expects is a matchers library for the `Expects <https://github.com/jaimegildesagredo/expects>`_ assertion library. It provides matchers for the `Doublex <https://pypi.python.org/pypi/doublex>`_ test double library.

Usage
=====

Just import the ``expect`` callable and the Doublex-Expects matchers and start writing assertions for test doubles.

Spies
-----

.. code-block:: python

    from expects import expect
    from doublex_expects import *
    from doublex import Spy

    my_spy = Spy()

    my_spy.method()

    expect(my_spy.method).to(have_been_called)

Mocks
-----

.. code-block:: python

    from expects import expect
    from doublex_expects import *
    from doublex import Mock

    with Mock() as my_mock:
        my_mock.reset()
        my_mock.add(1)

    my_mock.reset()
    my_mock.add(1)

    expect(my_mock).to(have_been_satisfied)

Matchers
========

have_been_called
----------------

Asserts that a spy has been called.

.. code-block:: python

    expect(my_spy.method).to(have_been_called)
    expect(my_spy.method).not_to(have_been_called)

have_been_called_with
---------------------

Asserts that a spy has been called with given arguments.

.. code-block:: python

    expect(my_spy.method).to(have_been_called_with('foo', key='bar'))
    expect(my_spy.method).to(have_been_called_with(a(str), key=match('\w+')))
    expect(my_spy.method).to(have_been_called_with(anything, key='bar'))
    expect(my_spy.method).to(have_been_called_with('foo', any_arg))
    expect(my_spy.method).not_to(have_been_called_with('bar', key='foo'))

Times called modifiers
----------------------

once
^^^^

Asserts that a spy has been called exactly *once*.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.once)
    expect(my_spy.method).to(have_been_called_with('foo').once)
    expect(my_spy.method).not_to(have_been_called.once)

twice
^^^^^

Asserts that a spy has been called exactly *twice*.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.twice)
    expect(my_spy.method).to(have_been_called_with('foo').twice)
    expect(my_spy.method).not_to(have_been_called.twice)

exactly
^^^^^^^

Asserts that a spy has been called exactly *n* times.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.exactly(3))
    expect(my_spy.method).to(have_been_called_with('foo').exactly(3))
    expect(my_spy.method).not_to(have_been_called.exactly(3))

max
^^^

Asserts that a spy has been called maximum of *n* times.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.max(2))
    expect(my_spy.method).to(have_been_called_with('foo').max(2))
    expect(my_spy.method).not_to(have_been_called.max(2))

min
^^^

Asserts that a spy has been called minimum of *n* times.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.min(2))
    expect(my_spy.method).to(have_been_called_with('foo').min(2))
    expect(my_spy.method).not_to(have_been_called.min(2))

have_been_satisfied
-------------------

Verifies that a mock calls have been satisfied.

.. code-block:: python

    expect(my_mock).to(have_been_satisfied)
    expect(my_mock).not_to(have_been_satisfied)

have_been_satisfied_in_any_order
--------------------------------

Verifies that a mock calls have been satisfied regardless of the execution order.

.. code-block:: python

    expect(my_mock).to(have_been_satisfied_in_any_order)
    expect(my_mock).not_to(have_been_satisfied_in_any_order)

Installation
============

You can install the last stable release from PyPI using *pip* or *easy_install*.

.. code-block:: bash

    $ pip install doublex-expects

Also you can install the latest sources from *Github*.

.. code-block:: bash

     $ pip install -e git+git://github.com/jaimegildesagredo/doublex-expects.git#egg=doublex-expects

Specs
=====

To run the specs you should install the testing requirements and then run ``mamba``.

.. code-block:: bash

    $ python setup.py develop
    $ pip install -r test-requirements.txt
    $ mamba
