# -*- coding: utf-8 -*-

import doublex
from expects import expect, be_a
from expects.testing import failure
from expects.texts import plain_enumerate

from doublex_expects import *


with describe('have_been_called_with'):
    with before.each:
        self.method = doublex.Spy().method
        self.arg1 = 1
        self.arg2 = 'foobar'
        self.kwargs = {'foo': 1, 'bar': 2}

    with it('should pass if called with positional arg'):
        self.method(self.arg1)

        expect(self.method).to(have_been_called_with(self.arg1))

    with it('should pass if called with multiple positional args'):
        self.method(self.arg1, self.arg2)

        expect(self.method).to(have_been_called_with(self.arg1, self.arg2))

    with it('should pass if called with keyword args'):
        self.method(**self.kwargs)

        expect(self.method).to(have_been_called_with(**self.kwargs))

    with it('should pass if called with positional and keyword args'):
        self.method(self.arg1, self.arg2, **self.kwargs)

        expect(self.method).to(have_been_called_with(self.arg1, self.arg2, **self.kwargs))

    with it('passes if called with positional arg matching matcher'):
        self.method(self.arg1)

        expect(self.method).to(have_been_called_with(be_a(type(self.arg1))))

    with it('passes if called with multiple positional args matching matchers'):
        self.method(self.arg1, self.arg2)

        expect(self.method).to(have_been_called_with(
            be_a(type(self.arg1)),
            be_a(type(self.arg2))))

    with it('passes if called with keyword args matching matchers'):
        self.method(**self.kwargs)

        expect(self.method).to(have_been_called_with(
            **{k: be_a(type(v)) for k,v in self.kwargs.items()}))

    with it('should fail if not called with positional arg'):
        self.method()

        with failure('to have been called with {!r}'.format(self.arg1)):
            expect(self.method).to(have_been_called_with(self.arg1))

    with it('should fail if not called with keyword args'):
        self.method()

        with failure('been called with {}'.format(plain_enumerate((), self.kwargs))):
            expect(self.method).to(have_been_called_with(**self.kwargs))

    with context('#negated'):
        with it('should pass if called with different positional arg'):
            self.method(self.arg1)

            expect(self.method).not_to(have_been_called_with(self.arg1, self.arg2))

        with it('should fail if called with args'):
            self.method(self.arg1, **self.kwargs)

            with failure('not to have been called with {}'.format(plain_enumerate((self.arg1,), self.kwargs))):
                expect(self.method).not_to(have_been_called_with(self.arg1, **self.kwargs))

    with describe('once'):
        with it('should pass if called with args once'):
            self.method(self.arg1)

            expect(self.method).to(have_been_called_with(self.arg1).once)

        with it('should pass if called with args once and with other args'):
            self.method(self.arg1)
            self.method()

            expect(self.method).to(have_been_called_with(self.arg1).once)

        with it('should fail if called with args more than once'):
            self.method(self.arg1)
            self.method(self.arg1)

            with failure('to have been called with {!r} once'.format(self.arg1)):
                expect(self.method).to(have_been_called_with(self.arg1).once)
