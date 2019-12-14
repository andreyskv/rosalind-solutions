# Finding a Spliced Motif


# Read FASTA format file
def read_fasta(filename):
    file = open(filename)
    sample = file.read()
    # Convert FASTA string into dictonary
    entries = dict(map(lambda e: [i.replace('\n', '') for i in e.split('\n', 1)][::-1], sample.lstrip('>').split('>')))
    return list(entries.keys())


dna_s, dna_t = read_fasta('Data/SSEQ.txt')

pt = 0
pts = []
for t in dna_t:
    pt = dna_s.find(t, pt)
    pt += 1
    pts.append(str(pt))

print(' '.join(pts))