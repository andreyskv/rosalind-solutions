# Independent Alleles
import math
# Probability of Aa genotype is 0.5 conveniently for every(!) generation so we do no need to iterate over generations.
p = 0.25 # AaBb is hence 0.5^0.5

k = 6   # Generation number
N = 17  # Number of children required to be AaBb genotype at gen k
n = pow(2,k)  # Total number of children at the last generation k

# It took me forever to realize that you can
# Apply binomial distribution formula to find at least N children out of T with exact probability of p
# sum_(x=N to n) (nCx * P^x * (1 – P)^(n – x))
res = round(sum(math.comb(n,i)*pow(p,i)*pow(1-p,n-i) for i in range(N, n+1)),3)
print(res)