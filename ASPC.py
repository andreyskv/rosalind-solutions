# Intorduction to alternative splicing

from math import comb  # Requires >= Python 3.8
N = 1814
k = 1093

# Solution is the sum of combinations for each subset of length k:N in N.
print(sum(comb(N, i) for i in range(k, N+1))% 1000000)