# -*- coding: utf-8 -*-

import doublex
from expects import expect
from expects.testing import failure

from doublex_expects import *


with describe('have_been_satisfied'):
    with it('passes if mock methods have been called in order'):
        with doublex.Mock() as mock:
            mock.foo(1)
            mock.bar()

        mock.foo(1)
        mock.bar()

        expect(mock).to(have_been_satisfied)

    with it('fails if mock methods have not been called'):
        with doublex.Mock() as mock:
            mock.foo(1)
            mock.bar()

        mock.foo(1)

        with failure:
            expect(mock).to(have_been_satisfied)

    with it('fails if mock methods have been called in another order'):
        with doublex.Mock() as mock:
            mock.foo(1)
            mock.bar()

        mock.bar()
        mock.foo(1)

        with failure:
            expect(mock).to(have_been_satisfied)
