# Introduction to Random Strings
from math import log10

s = 'CAAGGGATATGCCGCCAACGTGCGTTCGGTTGTGGCTAAGAAGTGGTCTGATGTGGCTGCCACGCCGACCCTTGTAAGTCTTCGATTGTTCGTTGAAGG'
probs = '0.099 0.134 0.220 0.236 0.325 0.388 0.469 0.507 0.580 0.626 0.702 0.717 0.811 0.828 0.889'
cgs = [float(x) for x in probs.split(' ')]

result = []
for cg in cgs:
    probs = [cg/2 if (x == 'C' or x == 'G') else (1-cg)/2 for x in s]
    result.append(round(sum(log10(x) for x in probs), 3))

print(' '.join(str(x) for x in result))


