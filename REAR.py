# Reversal distance

import time
start_time = time.time()

file = open('Data/REAR.txt')
sample = file.read()
pairs = [x.split('\n') for x in sample.split('\n\n')]
N = 10


# To normalize (x->12345678910 y->?) is to find position (i.e index) of element of string y in the string x.
# Example: if x = 12345678910 then for 13254769810 position of 2 in a is 3, which matches its current position so it is normzlized already
def normalize(x, y):
    return [x.index(i) + 1 for i in y]


# Find breakpoints for the list. Breakpoints are places where number jumps more than 1
# Something like described here http://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=1103&context=etd_projects
def breakpoint_cnt(x):
    count = 0
    breakpoints = []
    for i in range(0, N + 1):

        left = x[i - 1] if i > 0 else 0
        right = x[i] if i < N else N+1

        if abs(right - left) > 1:
            # count += 1
            breakpoints.append(i-1)
    return breakpoints


# Hamming distance betwen x and y is count of places where values don't match
def hamming_distance(x, y):
    return sum([j != x[i] for i, j in enumerate(y)])


def search(a1, b1, dist, c):
    global sol

    # new_dist = hamming_distance(a1, b1)  # Use hamming distance as pruning method (weaker but much faster convergence method)
    bps = breakpoint_cnt(b1)               # Use minimal breakpoint distance method (much stronger method but slow convergence for depth 9)
    new_dist = len(bps)
    if new_dist >= dist:  # Pruning to avoid full recursion. We cut this branch and exit if the new distance is not better than on the previous step.
        return
    elif new_dist == 0:   # We are done! The distance is 0 which means the new string matches the target exactly.
        sol = min(sol, c)
        return
    elif c == N-2 or c >= sol: # If 8 and we checked new_dist is not 0 than solution can only be 9. We cut it here.
        return
    else:
        c += 1             # The new distance is greater than the previous so we increment the counter and continue with this branch.

    for i in range(N-2):   # Loop over and create all possible reversal lists and use it as new a new input for search
        # for j in range(i + 1, N): # Loop if hamming distance pruning is used
        for j in bps:            # Look only at segments that end at breakpoints
            if j - i > 1:
                b1[i:j+1] = b1[i:j+1][::-1]
                search(a1, b, new_dist, c)
                b1[i:j + 1] = b1[i:j + 1][::-1]  # Intead of creating a copy of the list we revert b to original state for the next step


result = []
for p in pairs:
    K = 0
    sol = 9
    a = [int(x) for x in p[0].split(' ')]
    b = [int(x) for x in p[1].split(' ')]

    # start = hamming_distance(a, b)
    # search(a, b, start + 1, 0)

    b = normalize(b,a)
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # start = hamming_distance(a, b)
    start_bps = breakpoint_cnt(b)
    start = len(start_bps)
    search(a, b, start + 1, 0)

    print(sol)
    result.append(sol)

print (' '.join(str(x) for x in result))

print("time elapsed: {:.2f}s".format(time.time() - start_time))

