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
