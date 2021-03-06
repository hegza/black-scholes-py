## 31.1.-20
### Working on Arch Linux, pylon.
1. Set up Python and library dependencies for the Black-Scholes example using `conda`.
2. Intel MKL produced an issue with message:
```
INTEL MKL ERROR: /home/hegza/.conda/envs/modern-numerics/lib/python3.8/site-packages/mkl/../../../libmkl_core.so: invalid ELF header.
Intel MKL FATAL ERROR: Cannot load libmkl_core.so.
```
3. Install community package `intel-parallel-studio-xe` from AUR (2.8 GB).
4. Installation predicted to take 90 minutes over wireless. Swapping computers.

### Working on Windows, Etana.
1. `sympy.statistics` library dependency has been deprecated in favor of `sympy.stats`.
2. Replaced dependency.
3. Wrote unit tests, and breakage by API changes in sympy and scipy.
4. Implement a simple benchmark with quick results:
    * euro_vanilla: 0.16319392499999996
    * euro_vanilla_dividend: 0.16434525900000008
    * sym_euro_vanilla: 4.94602177
    * sym_euro_vanilla_dividend: 4.843446234

## 2.2.-20
### Resume working on Arch Linux, pylon
1. `conda install -c anaconda mkl` fixed the problem with Intel MKL. Probably because it replaced the .so with the incorrect ELF.
2. Run the benchmark with quick results (lots of stuff on background):
    * euro_vanilla: 0.25940795600035926
    * euro_vanilla_dividend: 0.2574756679969141
    * sym_euro_vanilla: 5.854757393994078
    * sym_euro_vanilla_dividend: 5.827031799999531

## 3.2.-20
### Windows, Etana
1. Remove dependency to sympy as out-of-scope.
2. Increase bench coverage to 100 %.

### Arch Linux, pylon
1. Apply Cython on `black_scholes_dp` and `timeit` via interpreter for quick results.
    * >>> print(str(timeit( lambda : black_scholes_dp.black_scholes_call_div(50, 100, 1, 0.05, 0.06, 0.25), number=1000 )/1000.0))
    * 0.0002949255430139601

## 15.3.-20
- Priced 288 million options in 15.737706999999318 seconds, using Intel MKL.
    * Verified that it's only using main memory (approx 13 Gb), did not go to swap.
    * 18,299,997.5791 billion options per second
    * 5.4644816e-8 seconds per option

