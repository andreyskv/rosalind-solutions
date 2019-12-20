# Partial Permutations
import math
from functools import reduce

k = 9
N = 96

print(math.perm(N,k) % 1000000)
print(reduce(lambda x, y: x*y % 1000000, range(N, N-k, -1)))
