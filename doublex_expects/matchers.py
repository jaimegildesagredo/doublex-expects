# -*- coding: utf-8 -*-

from expects import be_above_or_equal, be_below_or_equal
from expects.matchers import Matcher
from expects.texts import plain_enumerate

MAX_TIMES = be_below_or_equal
MIN_TIMES = be_above_or_equal


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
        self._times = MIN_TIMES(1)
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
        return self._match_value(self._times, len(self._calls_matching(subject)))

    def _calls_matching(self, subject):
        calls = []

        for call in subject.calls:
            if self._match_call(call):
                calls.append(call)

        return calls

    def _match_call(self, call):
        return self._match_args(call) and self._match_kwargs(call)

    def _match_args(self, call):
        for i, matcher in enumerate(self._args):
            if matcher == any_arg:
                return True

            try:
                arg = call.args[i]
            except IndexError:
                return False
            else:
                if not self._match_value(matcher, arg):
                    return False

        return True

    def _match_kwargs(self, call):
        for k, matcher in self._kwargs.items():
            try:
                value = call.kargs[k]
            except KeyError:
                return False
            else:
                if not self._match_value(matcher, value):
                    return False

        return True

    def _description(self, subject):
        message = 'have been called'

        if self._args or self._kwargs:
            message += ' with {}'.format(plain_enumerate(self._args, self._kwargs))


        if len(self._times_description) != 0:
            message += ' ' + self._times_description

        message += ' but calls that actually ocurred were:\n{}'.format(subject.double._recorded.show(indent=10))

        return message

have_been_called = _have_been_called()


class _anything(Matcher):
    def _match(self, subject):
        return True

anything = _anything()


class _any_arg(Matcher):
    def _match(self, subject):
        raise NotImplementedError()


any_arg = _any_arg()
