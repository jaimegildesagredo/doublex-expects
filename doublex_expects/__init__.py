# -*- coding: utf-8 -*-

import doublex


class Spy(object):
    def __init__(self, method, *_):
        self._method = method

    @property
    def to(self):
        return self

    @property
    def have(self):
        return self

    @property
    def been(self):
        return self

    @property
    def called(self):
        assert self._method._was_called(doublex.internal.InvocationContext(doublex.ANY_ARG), doublex.matchers.any_time), 'Expected {!r} to have been called'.format(self._method)

        return _Called(self._method)


class _Called(object):
    def __init__(self, method):
        self._method = method

    @property
    def once(self):
        assert self._times == 1, 'Expected {!r} to have been called once but was called {} times'.format(self._method, self._times)

    @property
    def _times(self):
        return self._method.double._recorded.count(
            doublex.internal.Invocation(
                self._method.double,
                self._method.name,
                doublex.internal.InvocationContext(doublex.ANY_ARG)))
