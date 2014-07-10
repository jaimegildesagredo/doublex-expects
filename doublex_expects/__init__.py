# -*- coding: utf-8 -*-

import doublex
from expects.expectation import Expectation, Proxy


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
        return _Called(self)

    @property
    def once(self):
        self._assert(self._times == 1,
                     'but was called {} times'.format(self._times))

    @property
    def twice(self):
        self._assert(self._times == 2,
                     'but was called {} times'.format(self._times))

    def exactly(self, times):
        self._assert(self._times == times, '{} times'.format(times))

    def max(self, times):
        self._assert(self._times <= times, '{} times'.format(times))

    def min(self, times):
        self._assert(self._times >= times, '{} times'.format(times))

    @property
    def _times(self):
        return self._actual.double._recorded.count(
            doublex.internal.Invocation(
                self._actual.double,
                self._actual.name,
                doublex.internal.InvocationContext(doublex.ANY_ARG)))

    def with_args(self, *args, **kwargs):
        self._assert(self._was_called_with_args(args, kwargs),
                     *self._get_message_for(args, kwargs))

    def _was_called_with_args(self, args, kwargs):
        return self._actual._was_called(
            doublex.internal.InvocationContext(*args, **kwargs),
            doublex.matchers.any_time)

    def _get_message_for(self, args, kwargs):
        result = []

        if len(args) > 0:
            result.append(repr(args))

        if len(kwargs) > 0:
            result.append(repr(kwargs))

        if len(result) == 2:
            result.insert(1, 'and')

        return result


class _Called(Proxy):
    def __call__(self):
        self._assert(self._was_called)

    @property
    def _was_called(self):
        return self._actual._was_called(
            doublex.internal.InvocationContext(doublex.ANY_ARG),
            doublex.matchers.any_time)
