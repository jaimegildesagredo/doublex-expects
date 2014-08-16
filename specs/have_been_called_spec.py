# -*- coding: utf-8 -*-

import doublex
from expects import expect
from expects.testing import failure

from doublex_expects import *


with describe('have_been_called'):
    with before.each:
        self.method = doublex.Spy().method

    with it('should pass if method called'):
        self.method()

        expect(self.method).to(have_been_called)

    with it('should pass if method called twice'):
        self.method()
        self.method()

        expect(self.method).to(have_been_called)

    with it('should fail if method not called'):
        with failure('to have been called'):
            expect(self.method).to(have_been_called)

    with context('#negated'):
        with it('should pass if not called'):
            expect(self.method).not_to(have_been_called)

        with it('should fail if called'):
            self.method()

            with failure('not to have been called'):
                expect(self.method).not_to(have_been_called)

    with describe('once'):
        with it('should pass if called once'):
            self.method()

            expect(self.method).to(have_been_called.once)

        with it('should fail if called more than once'):
            self.method()
            self.method()

            with failure('to have been called once'):
                expect(self.method).to(have_been_called.once)

        with context('#negated'):
            with it('should pass if called more than once'):
                self.method()
                self.method()

                expect(self.method).not_to(have_been_called.once)

            with it('should fail if called once'):
                self.method()

                with failure('not to have been called once'):
                    expect(self.method).not_to(have_been_called.once)

    with describe('twice'):
        with it('should pass if called twice'):
            self.method()
            self.method()

            expect(self.method).to(have_been_called.twice)

        with it('should fail if called more than twice'):
            self.method()
            self.method()
            self.method()

            with failure('to have been called twice'):
                expect(self.method).to(have_been_called.twice)

        with context('#negated'):
            with it('should pass if not called twice'):
                self.method()

                expect(self.method).not_to(have_been_called.twice)

            with it('should fail if called twice'):
                self.method()
                self.method()

                with failure('not to have been called twice'):
                    expect(self.method).not_to(have_been_called.twice)

    with describe('exactly'):
        with it('should pass if called exactly x times'):
            self.method()
            self.method()

            expect(self.method).to(have_been_called.exactly(2))

        with it('should fail if called a different amount of times'):
            self.method()

            with failure('to have been called exactly 2 times'):
                expect(self.method).to(have_been_called.exactly(2))

        with context('#negated'):
            with it('should pass if called a different amount of times'):
                self.method()

                expect(self.method).not_to(have_been_called.exactly(2))

            with it('should fail if called exactly x times'):
                self.method()
                self.method()

                with failure('not to have been called exactly 2 times'):
                    expect(self.method).not_to(have_been_called.exactly(2))

    with describe('max'):
        with it('should pass if called maximum x times'):
            self.method()
            self.method()
            self.method()
            self.method()

            expect(self.method).to(have_been_called.max(4))

        with it('should fail if called more times than the maximum'):
            self.method()
            self.method()
            self.method()

            with failure('to have been called max 2 times'):
                expect(self.method).to(have_been_called.max(2))

        with context('#negated'):
            with it('should pass if called more times than the maximum'):
                self.method()
                self.method()
                self.method()

                expect(self.method).not_to(have_been_called.max(2))

            with it('should fail if not called maximum x times'):
                self.method()

                with failure('not to have been called max 2 times'):
                    expect(self.method).not_to(have_been_called.max(2))

    with describe('min'):
        with it('should pass if called minimum x times'):
            self.method()
            self.method()
            self.method()
            self.method()

            expect(self.method).to(have_been_called.min(4))

        with it('should fail if called less times than the minimum'):
            self.method()

            with failure('to have been called min 2 times'):
                expect(self.method).to(have_been_called.min(2))

        with context('#negated'):
            with it('should pass if called less times than the minimun'):
                self.method()

                expect(self.method).not_to(have_been_called.min(2))

            with it('should fail if not called minimum x times'):
                self.method()
                self.method()

                with failure('not to have been called min 2 times'):
                    expect(self.method).not_to(have_been_called.min(2))
