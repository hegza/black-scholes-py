import numpy as np

import scipy.stats as si
import sympy as sy
import sympy.stats as systats


def black_scholes_call_div(S, K, T, r, q, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    call = (S * np.exp(-q * T) * si.norm.cdf(d1, 0.0, 1.0) -
            K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))

    return call


def black_scholes_put_div(S, K, T, r, q, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) -
           S * np.exp(-q * T) * si.norm.cdf(-d1, 0.0, 1.0))

    return put


def euro_vanilla_dividend(S, K, T, r, q, sigma, option='call'):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option == 'call':
        result = (S * np.exp(-q * T) * si.norm.cdf(d1, 0.0, 1.0) -
                  K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == 'put':
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) -
                  S * np.exp(-q * T) * si.norm.cdf(-d1, 0.0, 1.0))

    return result


def black_scholes_call_div_sym(S, K, T, r, q, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    N = systats.Normal("N", "N", 0.0, 1.0)

    d1 = (sy.ln(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))
    d2 = (sy.ln(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))

    call = S * sy.exp(-q * T) * N.cdf(d1) - K * sy.exp(-r * T) * N.cdf(d2)

    return call


def black_scholes_call_put_sym(S, K, T, r, q, sigma):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    N = systats.Normal("N", "N", 0.0, 1.0)

    d1 = (sy.ln(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))
    d2 = (sy.ln(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))

    put = K * sy.exp(-r * T) * N.cdf(-d2) - S * sy.exp(-q * T) * N.cdf(-d1)

    return put


def sym_euro_vanilla_dividend(S, K, T, r, q, sigma, option='call'):

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset
    # sigma: volatility of underlying asset

    N = systats.Normal("N", "N", 0.0, 1.0)

    d1 = (sy.ln(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))
    d2 = (sy.ln(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * sy.sqrt(T))

    if option == 'call':
        result = S * sy.exp(-q * T) * N.cdf(d1) - K * \
            sy.exp(-r * T) * N.cdf(d2)
    if option == 'put':
        result = K * sy.exp(-r * T) * N.cdf(-d2) - S * \
            sy.exp(-q * T) * N.cdf(-d1)

    return result
