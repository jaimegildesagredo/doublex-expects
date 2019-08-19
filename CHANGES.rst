Changes
=======

0.7.1 (2019-08-19)
------------------

Bug fixes
^^^^^^^^^^

* ``have_been_satisfied_in_any_order`` matcher failed in some cases. See issue `GH-19 <https://github.com/jaimegildesagredo/doublex-expects/issues/19>`_ and pull request `GH-20 <https://github.com/jaimegildesagredo/doublex-expects/pull/20>` for more info._

0.7.0 (2018-09-26)
------------------

Highlights
^^^^^^^^^^

* 0.7.0 final release with support for expects >= 0.8.0.


0.7.0rc2 (2015-10-26)
---------------------

Bug fixes
^^^^^^^^^

* Resolve error when passing an object with custom ``__eq__`` to ``have_been_called_with``. See `GH-10 <https://github.com/jaimegildesagredo/doublex-expects/issues/10>`_.

0.7.0rc1 (2015-07-17)
---------------------

Highlights
^^^^^^^^^^

* Work with expects >= 0.8.0rc1

0.6.0 (2015-06-26)
------------------

Highlights
^^^^^^^^^^

* Added ``have_been_satisfied`` and ``have_been_satisfied_in_any_order`` matchers to verify mocks::

    with Mock() as my_mock:
        my_mock.method(1)
        my_mock.method(2)

    my_mock.method(1)
    my_mock.method(2)

    expect(my_mock).to(have_been_satisfied)

* And::

    with Mock() as my_mock:
        my_mock.method(1)
        my_mock.method(2)

    my_mock.method(2)
    my_mock.method(1)

    expect(my_mock).to(have_been_satisfied_in_any_order)

0.5.0 (2015-01-13)
------------------

Highlights
^^^^^^^^^^

* Now another matchers can be passed as ``have_been_called_with`` arguments::

    my_spy = Spy()

    my_spy.method(1)

    expect(my_spy.method).to(have_been_called_with(an(int)))

* Added the ``anything`` matcher::

    expect(my_spy.method).to(have_been_called_with(anything))

* Added the ``any_arg`` special matcher::

    expect(my_spy.method).to(have_been_called_with(1, any_arg))

0.4.0 (2014-08-16)
------------------

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

0.3.0 (2014-07-11)
------------------

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

0.2.0 (2014-06-10)
------------------

Highlights
^^^^^^^^^^

* Use the new `expects type plugins <https://github.com/jaimegildesagredo/expects/commit/76c256a65e8112aa0740b1f15738fbd3653a6b4d>`_ for expectations.

0.1.0 (2014-06-05)
------------------

Highlights
^^^^^^^^^^

* First `doublex-expects` release.
