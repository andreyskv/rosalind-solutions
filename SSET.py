# Counting subsets
from math import comb  # Requires >= Python 3.8
N = 821

# Solution is the sum of combinations for each subset of length k in N.
print(sum(comb(N, i) for i in range(0, N + 1))% 1000000)