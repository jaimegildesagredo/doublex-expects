# -*- coding: utf-8 -*-

import doublex
from expects.matchers.matcher import Matcher


class HaveBeenCalled(Matcher):
    def with_args(self, *args, **kwargs):
        return CalledWithArgs(*args, **kwargs)

    @property
    def twice(self):
        return CalledTwice()

    @property
    def once(self):
        return CalledOnce()

    def min(self, times):
        return CalledMin(times)

    def max(self, times):
        return CalledMax(times)

    def exactly(self, times):
        return CalledExactly(times)

    def _match(self, subject):
        return subject._was_called(
            doublex.internal.InvocationContext(doublex.ANY_ARG),
            doublex.matchers.any_time)

    def _description(self, subject):
        return 'have been called'


class CalledExactly(Matcher):
    def __init__(self, times):
        self._times = times

    def _match(self, subject):
        return subject._was_called(
            doublex.internal.InvocationContext(doublex.ANY_ARG),
            self._times)

    def _description(self, subject):
        count = subject.double._recorded.count(
            doublex.internal.Invocation(
                subject.double,
                subject.name,
                doublex.internal.InvocationContext(doublex.ANY_ARG)))

        return 'have been called exactly {!r} times'.format(self._times)


class CalledMax(Matcher):
    def __init__(self, times):
        self._times = times

    def _match(self, subject):
        return subject._was_called(
            doublex.internal.InvocationContext(doublex.ANY_ARG),
            doublex.matchers.at_most(self._times))

    def _description(self, subject):
        count = subject.double._recorded.count(
            doublex.internal.Invocation(
                subject.double,
                subject.name,
                doublex.internal.InvocationContext(doublex.ANY_ARG)))

        return 'have been called max {!r} times'.format(self._times)


class CalledMin(Matcher):
    def __init__(self, times):
        self._times = times

    def _match(self, subject):
        return subject._was_called(
            doublex.internal.InvocationContext(doublex.ANY_ARG),
            doublex.matchers.at_least(self._times))

    def _description(self, subject):
        count = subject.double._recorded.count(
            doublex.internal.Invocation(
                subject.double,
                subject.name,
                doublex.internal.InvocationContext(doublex.ANY_ARG)))

        return 'have been called min {!r} times'.format(self._times)


class CalledOnce(Matcher):
    def _match(self, subject):
        return subject._was_called(
            doublex.internal.InvocationContext(doublex.ANY_ARG),
            1)

    def _description(self, subject):
        count = subject.double._recorded.count(
            doublex.internal.Invocation(
                subject.double,
                subject.name,
                doublex.internal.InvocationContext(doublex.ANY_ARG)))

        return 'have been called once but was called {!r} times'.format(count)


class CalledTwice(Matcher):
    def _match(self, subject):
        return subject._was_called(
            doublex.internal.InvocationContext(doublex.ANY_ARG),
            2)

    def _description(self, subject):
        count = subject.double._recorded.count(
            doublex.internal.Invocation(
                subject.double,
                subject.name,
                doublex.internal.InvocationContext(doublex.ANY_ARG)))

        return 'have been called twice but was called {!r} times'.format(count)


class CalledWithArgs(Matcher):
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def _match(self, subject):
        return subject._was_called(
            doublex.internal.InvocationContext(*self._args, **self._kwargs),
            doublex.matchers.any_time)

    def _description(self, subject):
        return 'have been called with args {}'.format(self._args_description)

    @property
    def _args_description(self):
        result = []

        if len(self._args) > 0:
            result.append(repr(self._args))

        if len(self._kwargs) > 0:
            result.append(repr(self._kwargs))

        if len(result) == 2:
            result.insert(1, 'and')

        return ' '.join(result)


have_been_called = HaveBeenCalled()
