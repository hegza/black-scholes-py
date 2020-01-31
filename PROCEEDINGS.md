## 31.1.-20
Working on Arch Linux, pylon.
1. Set up Python and library dependencies for the Black-Scholes example using `conda`.
2. Intel MKL produced an issue with message:
```
INTEL MKL ERROR: /home/hegza/.conda/envs/modern-numerics/lib/python3.8/site-packages/mkl/../../../libmkl_core.so: invalid ELF header.
Intel MKL FATAL ERROR: Cannot load libmkl_core.so.
```
    2.1. Install community package `intel-parallel-studio-xe` from AUR (2.8 GB).
    2.2. Installation predicted to take 90 minutes over wireless. Swapping computers.

Working on Windows, Etana.
1. sympy.statistics library dependency has been deprecated in favor of sympy.stats
    1.1. Replaced dependency
