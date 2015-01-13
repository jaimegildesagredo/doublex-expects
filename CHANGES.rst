Changes
=======

0.5.0 (Jan 13, 2015)
--------------------

Highlights
^^^^^^^^^^

* Now another matchers can be passed as ``have_been_called_with`` arguments::

    my_spy = Spy()

    my_spy.method(1)

    expect(my_spy.method).to(have_been_called_with(an(int)))

* Added the ``anything`` matcher::

    expect(my_spy.method).to(have_been_called_with(anything))

* Added the ``any_args`` special matcher::

    expect(my_spy.method).to(have_been_called_with(1, any_arg))

0.4.0 (Ago 16, 2014)
--------------------

Warnings
^^^^^^^^

This release *does not* maintain backwards compatibility with the previous version because was migrated to `expects 0.4.0 <http://expects.readthedocs.org/en/latest/changes.html#ago-15-2014>`_. **A migration in current assertions is required**. Matchers have been implemented maintaining compatibility with its equivalent assertions (and those that break compatibility are listed below).

Highlights
^^^^^^^^^^

* Now assert the times a method was called with the given args is possible. The ``have_been_called_with`` matcher supports *time modifiers*.
* The failure message now includes the method's calls that actually ocurred.

Backwards-incompatible
^^^^^^^^^^^^^^^^^^^^^^

* The previous ``to.have.been.called.with_args`` assertion was moved to its own matcher: ``have_been_called_with``. Also the ``have_been_called`` matcher can be used without being called.

0.3.0 (Jul 11, 2014)
--------------------

Highlights
^^^^^^^^^^

* Added the `called.with_args(*args, **kwargs)` assertion.
* Added the `called.min` and `called.max` assertions.
* Added the `called.twice` assertion.
* Python 3 and PyPy support.
* The `Expects` package should be installed independently.

Backwards-incompatible
^^^^^^^^^^^^^^^^^^^^^^

* The `called` assertion now should be "called" as a method: `expect(spy).to.have.been.called()`.

0.2.0 (Jun 10, 2014)
--------------------

Highlights
^^^^^^^^^^

* Use the new `expects type plugins <https://github.com/jaimegildesagredo/expects/commit/76c256a65e8112aa0740b1f15738fbd3653a6b4d>`_ for expectations.

0.1.0 (Jun 5, 2014)
-------------------

Highlights
^^^^^^^^^^

* First `doublex-expects` release.
