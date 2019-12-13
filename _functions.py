# Read FASTA format file
def read_fasta(filename):
    file = open(filename)
    sample = file.read()
    # Convert FASTA string into dictonary
    entries = dict(map(lambda e: [i.replace('\n', '') for i in e.split('\n', 1)][::-1], sample.lstrip('>').split('>')))
    return list(entries.keys())

# Read codon table file
def dna_codon_table():
    dna_codon_table_file = open("Data/DNA-codon-table.txt")
    dna_codon_table = dna_codon_table_file.read()
    dna_codon_list = list(filter(None, dna_codon_table.replace('   ','\n').split('\n'))) # Convert codon table to lookup dictionary
    return dict(map(lambda e: e.split(' '), dna_codon_list))

# Read sample file with one FASTA entry
def get_fasta(filename):
    file = open(filename)
    sample = file.read()
    # Read one entry FASTA format
    return [i.replace('\n', '') for i in sample.lstrip('>').split('\n', 1)][1]

def get_reverse_complement(p):
    nt = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([nt[n] for n in p[::-1]])

# Convert integer to Base of DNA nucleotides
def int2dnabase(x, ):
    d = ['A', 'C', 'G', 'T']  # ['0', '1', '2', '3']
    digits = []
    while x:
        digits.append(d[int(x % 4)])
        x = int(x / 4)

    digits.reverse()
    return ''.join(digits).rjust(3, d[0])


# Check if candidate string is in all list strings
def check_candidate_in_list(candidate, lst):
    return len([n for n in lst if candidate in n]) == len(lst)