# External imports
import numpy as np
import scipy.stats as si

from black_scholes_ndp import euro_vanilla_put

def main():
    put = euro_vanilla_put(50, 100, 1, 0.05, 0.25)
    print("put: " + str(put))

if __name__ =="__main__":
    main()

