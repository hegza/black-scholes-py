from timeit import timeit

from black_scholes_dp import *
from black_scholes_ndp import *


def bench_euro_vanilla_call():
    euro_vanilla_call(50, 100, 1, 0.05, 0.25)


def bench_euro_vanilla_put():
    euro_vanilla_put(50, 100, 1, 0.05, 0.25)


def bench_euro_vanilla():
    euro_vanilla(50, 100, 1, 0.05, 0.25, option='put')


def bench_black_scholes_call_div():
    black_scholes_call_div(50, 100, 1, 0.05, 0.06, 0.25)


def bench_black_scholes_put_div():
    black_scholes_put_div(50, 100, 1, 0.05, 0.06, 0.25)


def bench_euro_vanilla_dividend():
    euro_vanilla_dividend(50, 100, 1, 0.05, 0.06, 0.25, option='put')


print("euro_vanilla_call", str(timeit(bench_euro_vanilla_call, number=1000)))
print("euro_vanilla_put", str(timeit(bench_euro_vanilla_put, number=1000)))
print("euro_vanilla: " + str(timeit(bench_euro_vanilla, number=1000)))
print("black_scholes_call_div", str(
    timeit(bench_black_scholes_call_div, number=1000)))
print("black_scholes_put_div", str(
    timeit(bench_black_scholes_put_div, number=1000)))
print("euro_vanilla_dividend: " +
      str(timeit(bench_euro_vanilla_dividend, number=1000)))
