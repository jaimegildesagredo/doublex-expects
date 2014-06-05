# -*- coding: utf-8 -*-

import doublex
from expects import expect
from expects.testing import failure


with describe('called'):
    with before.each:
        self.method = doublex.Spy().method

    with it('should pass if method called'):
        self.method()

        expect(func=self.method).to.have.been.called

    with it('should pass if method called twice'):
        self.method()
        self.method()

        expect(func=self.method).to.have.been.called

    with it('should fail if method not called'):
        with failure(self.method, 'to have been called'):
            expect(func=self.method).to.have.been.called

    with context('#negated'):
        with it('should pass if not called'):
            expect(func=self.method).to.have.not_been.called

        with it('should fail if called'):
            self.method()

            with failure(self.method, 'to have not been called'):
                expect(func=self.method).to.have.not_been.called

    with describe('once'):
        with it('should pass if called once'):
            self.method()

            expect(func=self.method).to.have.been.called.once

        with it('should fail if called more than once'):
            self.method()
            self.method()

            with failure(
                self.method,
                'to have been called once but was called 2 times'):

                expect(func=self.method).to.have.been.called.once

        with context('#negated'):
            with it('should pass if called more than once'):
                self.method()
                self.method()

                expect(func=self.method).to.have.been.called.not_once

            with it('should fail if called once'):
                self.method()

                with failure(self.method, 'to have been called not once'):
                    expect(func=self.method).to.have.been.called.not_once

    with describe('exactly'):
        with it('should pass if called exactly x times'):
            self.method()
            self.method()

            expect(func=self.method).to.have.been.called.exactly(2)

        with it('should fail if called a different amount of times'):
            self.method()

            with failure(self.method, 'to have been called exactly 2 times'):
                expect(func=self.method).to.have.been.called.exactly(2)

        with context('#negated'):
            with it('should pass if called a different amount of times'):
                self.method()

                expect(func=self.method).to.have.been.called.not_exactly(2)

            with it('should fail if called exactly x times'):
                self.method()
                self.method()

                with failure(self.method, 'to have been called not exactly 2 times'):
                    expect(func=self.method).to.have.been.called.not_exactly(2)
