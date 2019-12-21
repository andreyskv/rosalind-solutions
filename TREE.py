#  Completing a Tree
N = 822  # Number of nodes

datafile = open('Data/TREE.txt')
data = datafile.read()
d = list(map(lambda e:  e.split(), data.split('\n')))

# The number of edges in a tree equals N-1 where N is the number of nodes
# Expected - Given number of edges is the solution. Dumb problem!
print(N-1-len(d))