===============
Doublex Expects
===============

.. image:: https://img.shields.io/pypi/v/doublex-expects.svg
    :target: https://pypi.python.org/pypi/doublex-expects
    :alt: Latest version

.. image:: https://img.shields.io/pypi/dm/doublex-expects.svg
    :target: https://pypi.python.org/pypi/doublex-expects
    :alt: Number of PyPI downloads

.. image:: https://secure.travis-ci.org/jaimegildesagredo/doublex-expects.svg?branch=master
    :target: http://travis-ci.org/jaimegildesagredo/doublex-expects

Doublex-Expects is a matchers library for the `Expects <https://github.com/jaimegildesagredo/expects>`_ assertion library. It provides matchers for the `Doublex <https://pypi.python.org/pypi/doublex>`_ test double library.

Installation
============

You can install the last stable release from PyPI using pip or easy_install.

.. code-block:: bash

    $ pip install doublex-expects

Also you can install the latest sources from Github.

.. code-block:: bash

     $ pip install -e git+git://github.com/jaimegildesagredo/doublex-expects.git#egg=doublex-expects

Usage
=====

Just import the ``expect`` callable and the Doublex-Expects matchers and start writing assertions for test doubles.

.. code-block:: python

    from expects import expect
    from doublex_expects import *
    from doublex import Spy

    my_spy = Spy()

    expect(my_spy.method).to(have_been_called)

Matchers
========

have_been_called
----------------

Assert that a spy has been called. Negation passes through.

.. code-block:: python

    expect(my_spy.method).to(have_been_called)
    expect(my_spy.method).not_to(have_been_called)

have_been_called.once
---------------------

Assert that a spy has been called exactly once.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.once)
    expect(my_spy.method).not_to(have_been_called.once)

have_been_called.twice
----------------------

Assert that a spy has been called exactly twice.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.twice)
    expect(my_spy.method).not_to(have_been_called.twice)

have_been_called.exactly
------------------------

Assert that a spy has been called exactly n times.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.exactly(3))
    expect(my_spy.method).not_to(have_been_called.exactly(3))


have_been_called.min
--------------------

Assert that a spy has been called minimum of `n` times.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.min(2))
    expect(my_spy.method).not_to(have_been_called.min(2))

have_been_called.max
--------------------

Assert that a spy has been called maximum of `n` times.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.max(2))
    expect(my_spy.method).not_to(have_been_called.max(2))

have_been_called.with_args
--------------------------

Assert that a spy has been called with given arguments.

.. code-block:: python

    expect(my_spy.method).to(have_been_called.with_args('foo', key='bar'))
    expect(my_spy.method).not_to(have_been_called.with_args('bar', key='foo'))

Specs
=====

To run the specs you should install the testing requirements and then run ``mamba``.

.. code-block:: bash

    $ python setup.py develop
    $ pip install -r test-requirements.txt
    $ mamba

License
=======

The Doublex-Expects is released under the `Apache2 license <http://www.apache.org/licenses/LICENSE-2.0.html>`_.
