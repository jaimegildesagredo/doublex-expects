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
