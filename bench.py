from timeit import timeit

from black_scholes_dp import *
from black_scholes_ndp import *


def bench_euro_vanilla():
    euro_vanilla(50, 100, 1, 0.05, 0.25, option='put')


def bench_euro_vanilla_dividend():
    euro_vanilla_dividend(50, 100, 1, 0.05, 0.06, 0.25, option='put')


def bench_sym_euro_vanilla():
    sym_euro_vanilla(50, 100, 1, 0.05, 0.25, option='put')


def bench_sym_euro_vanilla_dividend():
    sym_euro_vanilla_dividend(50, 100, 1, 0.05, 0.06, 0.25, option='put')


print("euro_vanilla: " + str(timeit(bench_euro_vanilla, number=1000)))
print("euro_vanilla_dividend: " +
      str(timeit(bench_euro_vanilla_dividend, number=1000)))
print("sym_euro_vanilla: " + str(timeit(bench_sym_euro_vanilla, number=1000)))
print("sym_euro_vanilla_dividend: " +
      str(timeit(bench_sym_euro_vanilla_dividend, number=1000)))
