# Finding a Shared Spliced Motif
# Levenshtein distance https://en.wikipedia.org/wiki/Levenshtein_distance

import time
start_time = time.time()


# Read FASTA format file
def read_fasta(filename):
    file = open(filename)
    sample = file.read()
    # Convert FASTA string into dictonary
    entries = dict(map(lambda e: [i.replace('\n', '') for i in e.split('\n', 1)][::-1], sample.lstrip('>').split('>')))
    return list(entries.keys())


s, t = read_fasta('Data/EDIT.txt')
s = ' ' + s  # Pad with space in front to prepare/align strings properly for building Levenshtein distance matrix
t = ' ' + t
sN, tN = len(s), len(t)

# Build Levenshtein matrix
m = [[0 for i in range(tN)] for j in range(sN)]
for i in range(1, sN):
    m[i][0] = i

for j in range(1, tN):
    m[0][j] = j

for i in range(1, sN):
    for j in range(1, tN):
        sub = 0 if s[i] == t[j] else 1
        m[i][j] = min((m[i-1][j] + 1, m[i][j-1] + 1, m[i-1][j-1] + sub))

print(m[-1][-1])    # The last last corner element is the edit distance.
print("time elapsed: {:.2f}s".format(time.time() - start_time))