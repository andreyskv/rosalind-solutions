# Read FASTA format file
file = open("Data/PDST.txt")
sample = file.read()

# Convert FASTA string into dictonary
entries = dict(map(lambda e:[i.replace('\n','') for i in e.split('\n',1)], sample.lstrip('>').split('>')))


# # P distance betwen x and y is percentage of places where values don't match
def p_distance(x, y):
    return round(sum([j != x[i] for i, j in enumerate(y)])/len(x), 5)


for k in entries.keys():
    row = []
    for l in entries.keys():
        d = p_distance(entries[k], entries[l])
        row.append(f'{d:.5f}')
    print(*row)