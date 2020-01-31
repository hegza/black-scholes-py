import unittest

from black_scholes_dp import *
from black_scholes_ndp import *


class MyTest(unittest.TestCase):
    def test_non_divident_paying(self):
        self.assertEqual(euro_vanilla_call(50, 100, 1, 0.05, 0.25),
                         0.027352509369436617
                         )
        self.assertEqual(euro_vanilla_put(50, 100, 1, 0.05, 0.25),
                         45.150294959440842
                         )
        self.assertEqual(euro_vanilla(50, 100, 1, 0.05, 0.25, option='put'),
                         45.150294959440842
                         )

    def test_non_divident_paying_sympy(self):
        # TODO: exact sympy variants untested
        pass

    def test_divident_paying(self):
        # TODO: divident paying variant untested
        pass

    def test_divident_paying_sympy(self):
        # TODO: exact sympy variants untested
        pass


if __name__ == '__main__':
    unittest.main()
