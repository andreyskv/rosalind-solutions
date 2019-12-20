# Sorting by reversals with BFS

from collections import deque
import time
start_time = time.time()

# a = [int(x) for x in '1 2 6 8 9 5 7 3 10 4'.split(' ')]
# b = [int(x) for x in '3 9 4 7 2 10 5 8 1 6'.split(' ')]
# a = [int(x) for x in '1 2 3 4 5 6 7 8 9 10'.split(' ')]
# b = [int(x) for x in '1 8 9 3 2 7 6 5 4 10'.split(' ')]
# a = [int(x) for x in '1 2 3 4 5 6 7 8 9 10'.split(' ')]
# b = [int(x) for x in '3 1 5 2 7 4 9 6 10 8'.split(' ')]

a = [int(x) for x in '10 5 2 4 1 7 3 9 6 8'.split(' ')]
b = [int(x) for x in '3 5 7 4 10 8 9 1 6 2'.split(' ')]
N = 10


# To normalize (x->12345678910 y->?) is to find position (i.e index) of element of string y in the string x.
# Example: if x = 12345678910 then for 13254769810 position of 2 in a is 3, which matches its current position so it is normzlized already
def normalize(x, y):
    return [x.index(i) + 1 for i in y]


# Find breakpoints for the list. Breakpoints are places where number jumps more than 1
# Something like described here http://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=1103&context=etd_projects
def breakpt(x):
    x.append(N+1)
    # breakpoints = tuple(i-1 for i in range(1, N + 1) if abs(x[i] - x[i - 1]) > 1)  # this is slower (??)
    breakpoints = []
    for i in range(1, N + 1):
        if abs(x[i] - x[i - 1]) > 1:
            breakpoints.append(i-1)
    x.pop()
    return breakpoints


# # # Hamming distance betwen x and y is number of places where values don't match
# def hamming_distance(x, y):
#     return sum([j != x[i] for i, j in enumerate(y)])
#

# Queue element will store the following tuple elements
# 0 current reversal
# 1 depth level
# 2 current reversal breakpoints
# 3 List of reversal steps [(i1, j1), (i2, j2), ...]

def search(b1):
    global rd, rd_steps

    bps = breakpt(b1)
    if len(bps) == 0:
        rd = 0
        return

    q = deque([(b1, 0, bps, [])])
    while q:

        b_cur, level, bps, steps = q.popleft()
        dist = len(bps)
        level += 1

        for i in range(N-2):   # Loop over and create all possible reversal lists and use it as new input for search
            # for j in range(i + 1, N):
            for j in bps:            # Look only at segments that end at breakpoints
                if j - i > 1:

                    b_new = b_cur.copy()
                    b_new[i:j+1] = b_new[i:j+1][::-1]

                    new_bps = breakpt(b_new)
                    new_dist = len(new_bps)

                    if new_dist >= dist:  # Pruning. If the new distance is not better than on the previous level then going to ignore this branch.
                        continue
                    elif new_dist == 0:  # We are done! The distance is 0 which means the new string matches the target exactly.
                        rd = level
                        steps.append((i+1, j+1))
                        rd_steps = steps
                        return

                    new_steps = steps.copy()
                    new_steps.append((i+1, j+1))
                    q.append((b_new, level, new_bps, new_steps))  # add to the queue only if potential candidate to find solution on the next level


b = normalize(a,b)

rd = 9  # Reversal distance. Initlize with maximum.
rd_steps = []

search(b)

print(rd)
for s in rd_steps[::-1]:
    print(s[0], s[1])
# print(rd_steps[::-1])
print("time elapsed: {:.2f}s".format(time.time() - start_time))
