# Transitions and Transversions


def read_fasta(filename):
    file = open(filename)
    sample = file.read()
    entries = dict(map(lambda e:[i.replace('\n', '') for i in e.split('\n', 1)][::-1], sample.lstrip('>').split('>')))
    return list(entries.keys())


[a, b] = read_fasta('Data/TRAN.txt')
m = {'A': 1, 'C': 4, 'G': 2, 'T': 5}  # Assign numbers to nucleotides to find transitions/transversions easily

diff = [abs(m[i] - m[j]) for i, j in zip(a, b)]
tranitions_c = len([x for x in diff if x == 1])   # Transition if difference is exactly 1
transversion_c = len([x for x in diff if x > 1])  # Transversion if it is not 0 or 1

print(tranitions_c/transversion_c)
