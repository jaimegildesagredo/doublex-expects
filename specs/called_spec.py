# -*- coding: utf-8 -*-

import doublex
from expects import expect
from expects.testing import failure


with describe('called'):
    with before.each:
        self.method = doublex.Spy().method
        self.arg1 = 1
        self.arg2 = 2
        self.kwargs = {'foo': 1, 'bar': 2}

    with it('should pass if method called'):
        self.method()

        expect(self.method).to.have.been.called()

    with it('should pass if method called twice'):
        self.method()
        self.method()

        expect(self.method).to.have.been.called()

    with it('should fail if method not called'):
        with failure('to have been called'):
            expect(self.method).to.have.been.called()

    with context('#negated'):
        with it('should pass if not called'):
            expect(self.method).to.have.not_been.called()

        with it('should fail if called'):
            self.method()

            with failure('to have not been called'):
                expect(self.method).to.have.not_been.called()

    with describe('once'):
        with it('should pass if called once'):
            self.method()

            expect(self.method).to.have.been.called.once

        with it('should fail if called more than once'):
            self.method()
            self.method()

            with failure('to have been called once but was called 2 times'):
                expect(self.method).to.have.been.called.once

        with context('#negated'):
            with it('should pass if called more than once'):
                self.method()
                self.method()

                expect(self.method).not_to.have.been.called.once

            with it('should fail if called once'):
                self.method()

                with failure('not to have been called once'):
                    expect(self.method).not_to.have.been.called.once

    with describe('twice'):
        with it('should pass if called twice'):
            self.method()
            self.method()

            expect(self.method).to.have.been.called.twice

        with it('should fail if called more than twice'):
            self.method()
            self.method()
            self.method()

            with failure('to have been called twice but was called 3 times'):
                expect(self.method).to.have.been.called.twice

        with context('#negated'):
            with it('should pass if not called twice'):
                self.method()

                expect(self.method).to.have.been.called.not_twice

            with it('should fail if called twice'):
                self.method()
                self.method()

                with failure('to have been called not twice'):
                    expect(self.method).to.have.been.called.not_twice

    with describe('exactly'):
        with it('should pass if called exactly x times'):
            self.method()
            self.method()

            expect(self.method).to.have.been.called.exactly(2)

        with it('should fail if called a different amount of times'):
            self.method()

            with failure('to have been called exactly 2 times'):
                expect(self.method).to.have.been.called.exactly(2)

        with context('#negated'):
            with it('should pass if called a different amount of times'):
                self.method()

                expect(self.method).not_to.have.been.called.exactly(2)

            with it('should fail if called exactly x times'):
                self.method()
                self.method()

                with failure('not to have been called exactly 2 times'):
                    expect(self.method).not_to.have.been.called.exactly(2)

    with describe('max'):
        with it('should pass if called maximum x times'):
            self.method()
            self.method()
            self.method()
            self.method()

            expect(self.method).to.have.been.called.max(4)

        with it('should fail if called more times than the maximum'):
            self.method()
            self.method()
            self.method()

            with failure('to have been called max 2 times'):
                expect(self.method).to.have.been.called.max(2)

        with context('#negated'):
            with it('should pass if called more times than the maximum'):
                self.method()
                self.method()
                self.method()

                expect(self.method).not_to.have.been.called.max(2)

            with it('should fail if not called maximum x times'):
                self.method()

                with failure('not to have been called max 2 times'):
                    expect(self.method).not_to.have.been.called.max(2)

    with describe('min'):
        with it('should pass if called minimum x times'):
            self.method()
            self.method()
            self.method()
            self.method()

            expect(self.method).to.have.been.called.min(4)

        with it('should fail if called less times than the minimum'):
            self.method()

            with failure('to have been called min 2 times'):
                expect(self.method).to.have.been.called.min(2)

        with context('#negated'):
            with it('should pass if called less times than the minimun'):
                self.method()

                expect(self.method).not_to.have.been.called.min(2)

            with it('should fail if not called minimum x times'):
                self.method()
                self.method()

                with failure('not to have been called min 2 times'):
                    expect(self.method).not_to.have.been.called.min(2)

    with describe('with_args'):
        with it('should pass if called with positional arg'):
            self.method(self.arg1)

            expect(self.method).to.have.been.called.with_args(self.arg1)

        with it('should pass if called with multiple positional args'):
            self.method(self.arg1, self.arg2)

            expect(self.method).to.have.been.called.with_args(self.arg1, self.arg2)

        with it('should pass if called with keyword args'):
            self.method(**self.kwargs)

            expect(self.method).to.have.been.called.with_args(**self.kwargs)

        with it('should pass if called with positional and keyword args'):
            self.method(self.arg1, self.arg2, **self.kwargs)

            expect(self.method).to.have.been.called.with_args(self.arg1, self.arg2, **self.kwargs)

        with it('should fail if not called with positional arg'):
            self.method()

            with failure('to have been called with args {!r}'.format((self.arg1,))):
                expect(self.method).to.have.been.called.with_args(self.arg1)

        with it('should fail if not called with keyword args'):
            self.method()

            with failure('been called with args {!r}'.format(self.kwargs)):
                expect(self.method).to.have.been.called.with_args(**self.kwargs)

        with context('#negated'):
            with it('should pass if called with different positional arg'):
                self.method(self.arg1)

                expect(self.method).not_been.called.with_args(self.arg1, self.arg2)

            with it('should fail if called with args'):
                self.method(self.arg1, **self.kwargs)

                with failure('not been called with args {!r} and {!r}'.format((self.arg1,), self.kwargs)):
                    expect(self.method).not_been.called.with_args(self.arg1, **self.kwargs)
