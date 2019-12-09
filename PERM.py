# Enumerating Gene Orders

n = 4
start = list(range(1,n+1))
res = []

def swap(i, j, ss):
    v = ss[j]
    ss[j] = ss[i]
    ss[i] = v
    return ss


# My backtracking. Swap each element with the last element
def permute(k, ss):

    if k == 0:
        return

    for i in range(0, k):
        ss1 = swap(i, k, ss.copy())
        permute(k-1, ss1)  # Permute for each root-1 child
        res.append(ss1)

    permute(k-1, ss)  # Need to permute for the current root element too


permute(n-1, start)
res.append(start)

print(len(res))
for e in res:
    print(' '.join(str(i) for i in e))