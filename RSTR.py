# Matching Random motifs
from functools import reduce

s = 'TTTGACACA'
cg = 0.440875
N = 98724

# Probability of occurance of each of the letter in 's' for the given CG content 'cg'
probs = [cg / 2 if (x == 'C' or x == 'G') else (1 - cg) / 2 for x in s]

# Probability of GC content is a product of all
pr = reduce((lambda x, y: x * y), probs)

# The chance of event with probability pr occuring in at least one of N attempts.
# It would be a probability of the event NOT occuring in N attempts subracted from 1 hence p=1-(1-pr)^N
pres = 1 - pow(1-pr, N)
print(round(pres,3))