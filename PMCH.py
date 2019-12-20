# Perfect Matchings and RNA Secondary Structures
from functools import reduce

sample = 'CUGGGAGGUCAAUUCCGUCACCGUAUAGAUACAGUGCCACAGGGCACUCGCGACUCUAGUGGUGACUACGUGCC'

# The formula for A-U or C-G appears to be n(n-1)(n-2)..1 where n is number of pairs (factorial! :))
# The total combinations would be a product of A-U and C-G matchings

au = sample.count('A')
cg = sample.count('C')

pmatchings = reduce(lambda x, y: y*x, range(1, au+1)) * reduce(lambda x, y: y*x, range(1, cg+1))
print(pmatchings)
