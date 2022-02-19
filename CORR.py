# Read FASTA format file
file = open("Data/CORR.txt")
sample = file.read()

# Convert FASTA string into dictonary
entries = dict(map(lambda e:[i.replace('\n','') for i in e.split('\n',1)], sample.lstrip('>').split('>')))


# Hamming distance betwen x and y is number of places where values don't match
def hamming_distance(x, y):
    return sum([j != x[i] for i, j in enumerate(y)])


# Complementing a Strand of DNA
def get_reverse_complement(p):
    nt = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([nt[n] for n in p[::-1]])


#string, reverse complement, isCorrect
dataset = [[v, get_reverse_complement(v), False] for v in entries.values()]
i = 0
for s1 in dataset:
    i += 1
    if not s1[2]:
        for s2 in dataset[i:]:
            if s1[0] == s2[0] or s1[1] == s2[0]:
                s1[2] = s2[2] = True
                break


good = list(filter(lambda x: (x[2] is True), dataset))
bad = list(filter(lambda x: (x[2] is False), dataset))
for s1 in bad:
    for s2 in good:
        if hamming_distance(s1[0], s2[0]) == 1:
            print(s1[0],"->",s2[0],sep="")
            break
        elif hamming_distance(s1[0], s2[1]) == 1:
            print(s1[0],"->",s2[1],sep="")
            break
