# Enumerating Oriented Gene Orderings
from itertools import permutations
N = 4

base = list(range(1,N+1))
sign_matrix = set()


# Build a set of tuples in the form of (1,1), (1,-1), (-1,1), (-1, -1) for N=2
# Important detail: tuples are hashable and can be used with sets unlike lists
def build_sign_matrix(seed, level):
    if level == N:
        return
    sign_matrix.add(seed)
    for i in range(0, N):
        build_sign_matrix(seed[:i] + (-1,) + seed[i+1:], level+1)


build_sign_matrix(tuple([1]*N), -1)

perms = []
for s in sign_matrix:
    start = [x*y for x,y in zip(s, base)]  # Apply each tuple to the base set and run permutations
    perms.extend(list(permutations(start)))  # Use built in tool for permutations instead writing own (see PERM)

print(len(perms))
print('\n'.join(' '.join(str(y) for y in x) for x in perms))
