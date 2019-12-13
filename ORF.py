# Open Reading Frames


# Read codon table file
def get_dna_codon_table():
    dna_codon_table_file = open("Data/DNA-codon-table.txt")
    dna_codon_table = dna_codon_table_file.read()
    dna_codon_list = list(filter(None, dna_codon_table.replace('   ','\n').split('\n'))) # Convert codon table to lookup dictionary
    return dict(map(lambda e: e.split(' '), dna_codon_list))


# Read sample file with one FASTA entry
def get_fasta():
    file = open('Data/ORF.txt')
    sample = file.read()
    # Read one entry FASTA format
    return [i.replace('\n', '') for i in sample.lstrip('>').split('\n', 1)][1]


# Return reverse complement of a string
def get_reverse_complement(p):
    nt = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([nt[n] for n in p[::-1]])


# Get all starting positions of ATG codon
def get_orf_all_starts(s):
    return [i for i in range(len(s)) if s.startswith('ATG', i)]


# Iterate string and check against codon lookup until Stop found
def get_protein_candidates(s):
    dcd = get_dna_codon_table()
    starts = get_orf_all_starts(s)
    proteins = []
    for pos in starts:
        prot = ''
        while pos < len(s)-3:
            ac = dcd[s[pos:pos + 3]]
            if ac == 'Stop':
                proteins.append(prot)
                break
            else:
                prot += ac
            pos += 3
    return proteins


# Main code starts
p = get_fasta()
revp = get_reverse_complement(p)
print('\n'.join(set(get_protein_candidates(p) + get_protein_candidates(revp))))

# print(p)
# print(revp)



