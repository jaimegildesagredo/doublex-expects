# -*- coding: utf-8 -*-

import doublex
from expects.expectation import Expectation


class Spy(Expectation):
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
        self._assert(self._was_called)

        return self

    @property
    def _was_called(self):
        return self._actual._was_called(
            doublex.internal.InvocationContext(doublex.ANY_ARG),
            doublex.matchers.any_time)

    @property
    def once(self):
        self._assert(self._times == 1,
                     'but was called {} times'.format(self._times))

    def exactly(self, times):
        self._assert(self._times == times, '{} times'.format(times))

    @property
    def _times(self):
        return self._actual.double._recorded.count(
            doublex.internal.Invocation(
                self._actual.double,
                self._actual.name,
                doublex.internal.InvocationContext(doublex.ANY_ARG)))
