# Locating Restriction Sites


# Read sample file with one FASTA entry
def get_fasta(filename):
    file = open(filename)
    sample = file.read()
    # Read one entry FASTA format
    return [i.replace('\n', '') for i in sample.lstrip('>').split('\n', 1)][1]


def get_reverse_complement(p):
    nt = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([nt[n] for n in p[::-1]])


dna = get_fasta('Data/REVP.txt')

for i in range(0, len(dna)):
    for l in range(4, len(dna) - i + 1, 2):
        p = dna[i:i + l]
        prev = get_reverse_complement(p)
        if p == prev:
            print(i + 1, l)


