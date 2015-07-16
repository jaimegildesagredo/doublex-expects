# -*- coding: utf-8 -*-

import doublex
from expects import expect, contain
from expects.testing import failure

from doublex_expects import *


with describe('have_been_called'):
    with before.each:
        self.method = doublex.Spy().method

    with it('passes if method called'):
        self.method()

        expect(self.method).to(have_been_called)

    with it('passes if method called twice'):
        self.method()
        self.method()

        expect(self.method).to(have_been_called)

    with it('fails if method not called'):
        with failure("calls were:\n          No one"):
            expect(self.method).to(have_been_called)

    with context('when negated'):
        with it('passes if not called'):
            expect(self.method).not_to(have_been_called)

        with it('fails if called'):
            self.method()

            with failure:
                expect(self.method).not_to(have_been_called)

    with describe('once'):
        with it('passes if called once'):
            self.method()

            expect(self.method).to(have_been_called.once)

        with it('fails if called more than once'):
            self.method()
            self.method()

            with failure:
                expect(self.method).to(have_been_called.once)

        with context('when negated'):
            with it('passes if called more than once'):
                self.method()
                self.method()

                expect(self.method).not_to(have_been_called.once)

            with it('fails if called once'):
                self.method()

                with failure:
                    expect(self.method).not_to(have_been_called.once)

    with describe('twice'):
        with it('passes if called twice'):
            self.method()
            self.method()

            expect(self.method).to(have_been_called.twice)

        with it('fails if called more than twice'):
            self.method()
            self.method()
            self.method()

            with failure:
                expect(self.method).to(have_been_called.twice)

        with context('when negated'):
            with it('passes if not called twice'):
                self.method()

                expect(self.method).not_to(have_been_called.twice)

            with it('fails if called twice'):
                self.method()
                self.method()

                with failure:
                    expect(self.method).not_to(have_been_called.twice)

    with describe('exactly'):
        with it('passes if called exactly x times'):
            self.method()
            self.method()

            expect(self.method).to(have_been_called.exactly(2))

        with it('passes if method called exactly 0 times'):
            expect(self.method).to(have_been_called.exactly(0))

        with it('fails if called a different amount of times'):
            self.method()

            with failure:
                expect(self.method).to(have_been_called.exactly(2))

        with context('when negated'):
            with it('passes if called a different amount of times'):
                self.method()

                expect(self.method).not_to(have_been_called.exactly(2))

            with it('fails if called exactly x times'):
                self.method()
                self.method()

                with failure:
                    expect(self.method).not_to(have_been_called.exactly(2))

    with describe('max'):
        with it('passes if called maximum x times'):
            self.method()
            self.method()
            self.method()
            self.method()

            expect(self.method).to(have_been_called.max(4))

        with it('fails if called more times than the maximum'):
            self.method()
            self.method()
            self.method()

            with failure:
                expect(self.method).to(have_been_called.max(2))

        with context('when negated'):
            with it('passes if called more times than the maximum'):
                self.method()
                self.method()
                self.method()

                expect(self.method).not_to(have_been_called.max(2))

            with it('fails if not called maximum x times'):
                self.method()

                with failure:
                    expect(self.method).not_to(have_been_called.max(2))

    with describe('min'):
        with it('passes if called minimum x times'):
            self.method()
            self.method()
            self.method()
            self.method()

            expect(self.method).to(have_been_called.min(4))

        with it('fails if called less times than the minimum'):
            self.method()

            with failure:
                expect(self.method).to(have_been_called.min(2))

        with context('when negated'):
            with it('passes if called less times than the minimun'):
                self.method()

                expect(self.method).not_to(have_been_called.min(2))

            with it('fails if not called minimum x times'):
                self.method()
                self.method()

                with failure:
                    expect(self.method).not_to(have_been_called.min(2))
