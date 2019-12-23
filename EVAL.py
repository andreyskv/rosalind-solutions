# Expected Number of Restriction Sites

from functools import reduce

N = 946636
s = 'TTCCAGGGCG'
probs = '0.000 0.093 0.117 0.204 0.256 0.314 0.335 0.381 0.440 0.509 0.542 0.598 0.640 0.712 0.775 0.800 0.873 0.926 1.000'

# N = 10
# s = 'AG'
# probs = '0.25 0.5 0.75'

cgs = [float(x) for x in probs.split(' ')]

res = []
for cg in cgs:
    prob = reduce(lambda x, y: x * y, [cg / 2 if (x == 'C' or x == 'G') else (1 - cg) / 2 for x in s])  # Probability of string with this gc content for N=len(s)
    res.append(round(prob*(N-len(s)+1), 4))  # Problem probability is sum of probabilities as many times as s can fit in t once, which is N-len(s)+1

print(' '.join(str(x) for x in res))

