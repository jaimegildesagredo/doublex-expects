Changes
=======

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
