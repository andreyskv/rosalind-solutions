# k-Mer composition
import re

def get_fasta(filename):
    file = open(filename)
    s = file.read()
    return [i.replace('\n', '') for i in s.lstrip('>').split('\n', 1)][1]


sample = get_fasta('Data/KMER.txt')
nucleotides = 'A C G T'.split(' ')
N = len(nucleotides)
kmer = [None]*N
kmer_composition = []


def iterate(pos):
    if pos == N:  # Once reached N the kmer string building is complete.
        kmer_str = ''.join(kmer)
        kmer_composition.append(str(len(re.findall(f'(?={kmer_str})', sample))))  # kmer with verlapping ocurrences
        return
    for n in nucleotides:
        kmer[pos] = n
        iterate(pos + 1)


iterate(0)
print(' '.join(kmer_composition))
