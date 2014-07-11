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

This is an addon plugin for the `Expects <https://github.com/jaimegildesagredo/expects>`_ assertion library. It provides assertions for the `Doublex <https://pypi.python.org/pypi/doublex>`_ test double library.

Installation
============

First you need to have `Expects <https://github.com/jaimegildesagredo/expects>`_ installed.

.. code-block:: bash

    $ pip install expects>=0.3

You can install the last stable release of Doublex-Expects from PyPI using pip or easy_install.

.. code-block:: bash

    $ pip install doublex-expects

Also you can install the latest sources from Github.

.. code-block:: bash

     $ pip install -e git+git://github.com/jaimegildesagredo/doublex-expects.git#egg=doublex-expects


Usage
=====

There is nothing special you need to do. Just import the ``expect`` callable and start writing assertions for test doubles.

.. code-block:: python

    from expects import expect
    from doublex import Spy

    my_spy = Spy()

    expect(my_spy.method).to.have.been.called()

Assertions
==========


called
------

Assert that a spy has been called. Negation passes through.

.. code-block:: python

	expect(my_spy.method).to.have.been.called()
	expect(my_spy.method).to.have.not_been.called()

Note that ``called`` can be used as a chainable property.

once
----

Assert that a spy has been called exactly once.

.. code-block:: python

	expect(my_spy.method).to.have.been.called.once
	expect(my_spy.method).not_to.have.been.called.once

twice
-----

Assert that a spy has been called exactly twice.

.. code-block:: python

	expect(my_spy.method).to.have.been.called.twice
	expect(my_spy.method).not_to.have.been.called.twice

exactly
-------

Assert that a spy has been called exactly n times.

.. code-block:: python

	expect(my_spy.method).to.have.been.called.exactly(3)
	expect(my_spy.method).not_to.have.been.called.exactly(3)


min
---

Assert that a spy has been called minimum of `n` times.

.. code-block:: python

	expect(my_spy.method).to.have.been.called.min(2)
	expect(my_spy.method).not_to.have.been.called.min(2)

max
---

Assert that a spy has been called maximum of `n` times.

.. code-block:: python

	expect(my_spy.method).to.have.been.called.max(2)
	expect(my_spy.method).not_to.have.been.called.max(2)

with_args
---------

Assert that a spy has been called with given arguments.

.. code-block:: python

	expect(my_spy.method).to.have.been.called.with_args('foo', key='bar')
	expect(my_spy.method).not_to.have.been.called.with_args('bar', key='foo')

Specs
=====

To run the specs you should install the testing requirements and then run `mamba`.

.. code-block:: bash

    $ python setup.py develop
    $ pip install -r test-requirements.txt
    $ mamba

License
=======

The Doublex-Expects is released under the `Apache2 license <http://www.apache.org/licenses/LICENSE-2.0.html>`_.
