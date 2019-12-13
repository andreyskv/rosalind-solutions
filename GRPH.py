#Overlap Graphs

# Read FASTA format file
file = open("Data/GRPH.txt")
sample = file.read()
# Convert FASTA string into dictonary
entries = dict(map(lambda e:[i.replace('\n','') for i in e.split('\n',1)][::-1], sample.lstrip('>').split('>')))

# Graph overlap O3
k = 3
dnas = list(entries.keys())

# Find matching strings comparing suffixes with prefixes and vice versa. Iterate down with the reduced internal loop.
for d in dnas:
    for d2 in dnas[dnas.index(d)+1:]:
        if d[-k:] == d2[:k]:
            print(entries[d], entries[d2])
        elif d[:k] == d2[-k:]:
            print(entries[d2], entries[d])