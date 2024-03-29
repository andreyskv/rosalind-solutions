# Interleaving Two Motifs
# Based on LCSQ problem
# First find the longest common subsequence (LCSQ) and then insert noncommon (not in LCSQ) values from both strings into LCSQ in the right order

#s = "ATCTGAT"
#t = "TGCATA"

#s = "ATTTTTG"
#t = "GTTTTTA"

s = "TATGGAGTATACATTCAATTTCTCCTATACTCGACGACTCCAGGCTTGCTGGGTTGGCTTACCCCACGCAGGAGGCTGACAGCGTGATA"
t = "AGAGAGTTACGAAGATGTATTGATTATTTAATGTCATCTCTAGCATCTCTCCACGCGAGGGGCCCTGATGCTTCGGAAACCACGCAAC"

# First solve for LCSQ using Needleman–Wunsch algorithm (matrix traverse)  (see LCSQ.py)
sN, tN = len(s), len(t)  # Size of the matrix

# Initial matrix sN+1 x tN+1 with zeros
m = [[0 for i in range(tN + 1)] for j in range(sN + 1)]

# Build it if current letter is same in both 's' and 't' then take the previous cell and icrement by 1 otherwise take maximum of upper or left cell
for i in range(1, sN+1):
    for j in range(1, tN+1):
        m[i][j] = 1 + m[i-1][j-1] if s[i-1] == t[j-1] else max(m[i-1][j], m[i][j-1])


# Now path through the matrix from the bottom right corner to the top left as per the DP algorithm
r = ''
i, j = sN, tN
while i > 0 and j > 0:
    l, d, u = m[i-1][j], m[i-1][j-1], m[i][j-1]  # left, diagonal and up elements relative to m[i][j]
    if l < m[i][j] > u and m[i][j] > d:  # if greater than diagonal and also greater than any sides we take it and move diagonally.
        i -= 1
        j -= 1
        r += s[i]  # build the string, alternatively r += t[j]
    elif m[i][j] == l:  # Move in the direction of the largest number in the matrix
        i -= 1
    elif m[i][j] == u:  # Move in the direction of the largest number in the matrix
        j -= 1

#Our longest common subsequence
lcsq = r[::-1]
print(lcsq)
#print(s)
#print(t)

scsp = ''
si_prev = ti_prev = -1
for n in lcsq:
    si = s.find(n, si_prev+1)
    ssub = s[si_prev+1:si]
    ti = t.find(n, ti_prev+1)
    tsub = t[ti_prev+1:ti]
    scsp += (ssub+tsub+n)
    ti_prev = ti
    si_prev = si

scsp += s[si_prev+1:]
scsp += t[ti_prev+1:]
print(scsp)
