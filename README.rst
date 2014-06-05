Doublex Expects
===============

.. image:: http://img.shields.io/pypi/v/doublex-expects.svg
    :target: https://pypi.python.org/pypi/doublex-expects
    :alt: Latest version

.. image:: http://img.shields.io/pypi/dm/doublex-expects.svg
    :target: https://pypi.python.org/pypi/doublex-expects
    :alt: Number of PyPI downloads

.. image:: https://secure.travis-ci.org/jaimegildesagredo/doublex-expects.png?branch=master
    :target: http://travis-ci.org/jaimegildesagredo/doublex-expects

**Doublex-expects** is an `Expects <https://github.com/jaimegildesagredo/expects>`_ plugin for `Doublex <https://pypi.python.org/pypi/doublex>`_ test doubles assertions.

Usage
-----

Just import the ``expect`` callable and start writing assertions for test doubles.

.. code-block:: python

    from expects import expect
    from doublex import Spy

    my_spy = Spy()

    expect(func=my_spy.method).to.have.been.called

    expect(func=my_spy.method).to.have.not_been.called

    expect(func=my_spy.method).to.have.been.called.once

    expect(func=my_spy.method).to.have.been.called.exactly(2)

Installation
------------

You can install the last stable release of Doublex-Expects from PyPI using pip or easy_install.

.. code-block:: bash

    $ pip install doublex-expects

Also you can install the latest sources from Github.

.. code-block:: bash

     $ pip install -e git+git://github.com/jaimegildesagredo/doublex-expects.git#egg=doublex-expects

Specs
-----

To run the specs you should install the testing requirements and then run `mamba`.

.. code-block:: bash

    $ pip install -r test-requirements.txt
    $ mamba

License
-------

The Doublex-Expects is released under the `Apache2 license <http://www.apache.org/licenses/LICENSE-2.0.html>`_.
