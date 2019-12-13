# Consensus and Profile

# Read FASTA format file
file = open("Data/CONS.txt")
sample = file.read()
# Convert FASTA string into dictonary
entries = dict(map(lambda e:[i.replace('\n','') for i in e.split('\n',1)][::-1], sample.lstrip('>').split('>')))
dna_list = list(entries.keys())

n = len(dna_list[0])
nt = {'A': [0]*n, 'C': [0]*n, 'G': [0]*n, 'T': [0]*n}


for d in dna_list:
    for i in range(0, n):
        nt[d[i]][i] += 1

consensus = ''.join([max(nt, key = lambda k: nt[k][i]) for i in range(0, n)])  # Find maximum across columns

print(consensus)
for v in nt:
    print(v+':', ' '.join(str(i) for i in nt[v]))
