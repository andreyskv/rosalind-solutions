# Rabbits and Recurrence Relations

N = 30; K = 4

p = [1, 0]  # Population p0 is # of children; p1 is # of adults
for n in range(1, N):
    gen = p[1]
    p[1] += p[0]
    p[0] = K*gen
    print(p[:])

print(sum(p[:]))
