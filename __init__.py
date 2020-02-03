from black_scholes_dp import *
from black_scholes_ndp import *


def main():
    euro_vanilla_call(50, 100, 1, 0.05, 0.25)
    euro_vanilla_put(50, 100, 1, 0.05, 0.25)
    euro_vanilla(50, 100, 1, 0.05, 0.25, option='put')
    black_scholes_call_div(50, 100, 1, 0.05, 0.06, 0.25)
    black_scholes_put_div(50, 100, 1, 0.05, 0.06, 0.25)
    euro_vanilla_dividend(50, 100, 1, 0.05, 0.06, 0.25, option='put')
