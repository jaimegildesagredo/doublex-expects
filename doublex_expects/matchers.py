# -*- coding: utf-8 -*-

from expects import be_above_or_equal, be_below_or_equal
from expects.matchers import Matcher, default_matcher
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
        result, _ = default_matcher(self._times)._match(len(self._calls_matching(subject)))
        reasons = ['calls were:']
        if not subject.double._recorded:
            reasons.append('No one')
        else:
            reasons.extend([str(i) for i in subject.double._recorded])
        return result, reasons

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
            if matcher is any_arg:
                return True

            try:
                arg = call.args[i]
            except IndexError:
                return False
            else:
                matcher = default_matcher(matcher)
                result, _ = matcher._match(arg)
                if not result:
                    return False

        return True

    def _match_kwargs(self, call):
        for k, matcher in self._kwargs.items():
            try:
                value = call.kargs[k]
            except KeyError:
                return False
            else:
                matcher = default_matcher(matcher)
                result, _ = matcher._match(value)
                if not result:
                    return False

        return True

    def __repr__(self):
        message = 'have been called'

        if self._args or self._kwargs:
            message += ' with {}'.format(plain_enumerate(self._args, self._kwargs))


        if len(self._times_description) != 0:
            message += ' ' + self._times_description

        return message


have_been_called = _have_been_called()


class _have_been_satisfied(Matcher):
    def _match(self, mock):
        reasons = ['expected calls were:']
        reasons.extend(["    {}".format(i) for i in mock._stubs])
        reasons.append('and actual calls were:')
        reasons.extend(["    {}".format(i) for i in mock._recorded])

        return mock._stubs == mock._recorded, reasons

have_been_satisfied = _have_been_satisfied()


class _have_been_satisfied_in_any_order(Matcher):
    def _match(self, mock):
        reasons = ['expected calls were:']
        reasons.extend(["    {}".format(i) for i in mock._stubs])
        reasons.append('and actual calls were:')
        reasons.extend(["    {}".format(i) for i in mock._recorded])

        return sorted(mock._stubs, key=str) == sorted(mock._recorded, key=str), reasons


have_been_satisfied_in_any_order = _have_been_satisfied_in_any_order()


class _anything(Matcher):
    def _match(self, subject):
        return True, []

anything = _anything()


class _any_arg(Matcher):
    def _match(self, subject):
        raise NotImplementedError()


any_arg = _any_arg()
