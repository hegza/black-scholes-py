import numpy as np
import scipy.stats as si


from numpy import float64
def euro_vanilla_call(S: int, K: int, T: int, r: float, sigma: float) -> float64:

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K *
            np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))

    return call


def euro_vanilla_put(S: int, K: int, T: int, r: float, sigma: float) -> float64:

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) -
           S * si.norm.cdf(-d1, 0.0, 1.0))

    return put


def euro_vanilla(S: int, K: int, T: int, r: float, sigma: float, option: str = 'call') -> float64:

    # S: spot price
    # K: strike price
    # T: time to maturity
    # r: interest rate
    # sigma: volatility of underlying asset

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option == 'call':
        result = (S * si.norm.cdf(d1, 0.0, 1.0) - K *
                  np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == 'put':
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) -
                  S * si.norm.cdf(-d1, 0.0, 1.0))

    return result
