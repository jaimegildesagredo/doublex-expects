# -*- coding: utf-8 -*-

import doublex
from expects.matchers import Matcher
from expects.texts import plain_enumerate

ANY_TIME = doublex.matchers.any_time
MAX_TIMES = doublex.matchers.at_most
MIN_TIMES = doublex.matchers.at_least


class _have_been_called(Matcher):
    @property
    def twice(self):
        return self._called.twice

    @property
    def once(self):
        return self._called.once

    def min(self, times):
        return self._called.min(times)

    def max(self, times):
        return self._called.max(times)

    def exactly(self, times):
        return self._called.exactly(times)

    def _match(self, subject):
        return self._called._match(subject)

    def _description(self, subject):
        return self._called._description(subject)

    @property
    def _called(self):
        return have_been_called_with()


class have_been_called_with(Matcher):
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._times = ANY_TIME
        self._times_description = ''

    @property
    def once(self):
        self._times = 1
        self._times_description = 'once'
        return self

    @property
    def twice(self):
        self._times = 2
        self._times_description = 'twice'
        return self

    def exactly(self, times):
        self._times = times
        self._times_description = 'exactly {} times'.format(times)
        return self

    def max(self, times):
        self._times = MAX_TIMES(times)
        self._times_description = 'max {} times'.format(times)
        return self

    def min(self, times):
        self._times = MIN_TIMES(times)
        self._times_description = 'min {} times'.format(times)
        return self

    def _match(self, subject):
        return subject._was_called(self.__args, self._times)

    @property
    def __args(self):
        if self._args or self._kwargs:
            return doublex.internal.InvocationContext(*self._args, **self._kwargs)
        return doublex.internal.InvocationContext(doublex.ANY_ARG)

    def _description(self, subject):
        message = 'have been called'

        if self._args or self._kwargs:
            message += ' with {}'.format(plain_enumerate(self._args, self._kwargs))

        message += ' ' + self._times_description
        message += ' but calls that actually ocurred were:\n{}'.format(subject.double._recorded.show(indent=10))

        return message

have_been_called = _have_been_called()
