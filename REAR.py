# a = [int(x) for x in '3 10 8 2 5 4 7 1 6 9'.split(' ')]
# b = [int(x) for x in '5 2 3 1 7 4 10 8 6 9'.split(' ')]

# to_identity = {value: i + 1 for i, value in enumerate(a)}
# normalized_perm = [to_identity[value] for value in b]
# # print(normalized_perm)
# # print('\n')

file = open('Data/REAR.txt')
sample = file.read()
pairs = [x.split('\n') for x in sample.split('\n\n')]
N = 10
K = 0  # Pruning stricktness (can be 0 or 1). We need this to search again if did not find solution with 0, which is much faster.
solutions = set([N-1])


# Hamming distance betwen x and y is count of places where values don't match
def hamming_distance(x, y):
    return sum([j != x[i] for i, j in enumerate(y)])


def search(a1, b1, dist, c):

    new_dist = hamming_distance(a1, b1)
    if new_dist >= dist + K:  # The critical part to avoid infinite recursion. We cut this branch and exit if the new hamming distance is worse (>= for K=0 or > for K=1) than on the previous step.
        return
    elif new_dist == 0 or c > min(solutions):   # We are done! The hamming distance is 0 which means the new string matches the target exactly. Or anything above 9 is wrong.
        # print(c)
        solutions.add(c)
        return
    else:
        c += 1            # The new hamming distance is greater than the previous so we increment counter and accept this branch to continue iterating on it.

    for i in range(N-2):   # Loop over and create all possible reversal lists and use it as new a new input for search
        for j in range(i + 1, N):
            # print(i,j+1)
            b2 = b1.copy()
            b2[i:j+1] = b2[i:j+1][::-1]
            search(a1, b2, new_dist, c)


# start = hamming_distance(a, b)
# search(a, b, start + 1, 0)
# search(b, a, start + 1, 0)
# print(min(solutions))
result=[]
for p in pairs:
    K = 0
    a = [int(x) for x in p[0].split(' ')]
    b = [int(x) for x in p[1].split(' ')]
    solutions = set([N-1])
    start = hamming_distance(a, b)
    search(a, b, start + 1, 0)
    search(b, a, start + 1, 0)
    if not solutions:
        K = 1
        print('K=', K)
        search(a, b, start + 1, 0)
        search(b, a, start + 1, 0)

    print(min(solutions))
    result.append(min(solutions))

print (' '.join(str(x) for x in result))


#
# def reversals(a, b):
#     c = 0
#     for i in range(10):
#         j = b.index(a[i])
#         if j != i:
#             b[i:j + 1] = b[i:j + 1][::-1]
#             c += 1
#             print(b)
#     return c
#
#

