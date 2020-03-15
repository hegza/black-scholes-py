# External imports
from timeit import timeit

# Module imports
from black_scholes_dp import *
from black_scholes_ndp import *


def bench_euro_vanilla_call():
    return euro_vanilla_call(50, 100, 1, 0.05, 0.25)


def bench_euro_vanilla_put():
    return euro_vanilla_put(50, 100, 1, 0.05, 0.25)


def bench_euro_vanilla():
    return euro_vanilla(50, 100, 1, 0.05, 0.25, option='put')


def bench_black_scholes_call_div():
    return black_scholes_call_div(50, 100, 1, 0.05, 0.06, 0.25)


def bench_black_scholes_put_div():
    return black_scholes_put_div(50, 100, 1, 0.05, 0.06, 0.25)


def bench_euro_vanilla_dividend():
    return euro_vanilla_dividend(50, 100, 1, 0.05, 0.06, 0.25, option='put')


print("euro_vanilla_put", str(timeit(bench_euro_vanilla_put, number=100000)/100000.))