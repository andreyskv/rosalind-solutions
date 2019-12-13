# RNA Splicing


# Read FASTA format file
def read_fasta(filename):
    file = open(filename)
    sample = file.read()
    # Convert FASTA string into dictonary
    entries = dict(map(lambda e: [i.replace('\n', '') for i in e.split('\n', 1)][::-1], sample.lstrip('>').split('>')))
    return list(entries.keys())


# Read codon table file
def get_codon_table(filename):
    codon_table_file = open(filename)
    codon_table = codon_table_file.read()
    codon_list = list(filter(None, codon_table.replace('   ','\n').split('\n'))) # Convert codon table to lookup dictionary
    return dict(map(lambda e: e.split(' '), codon_list))


data = read_fasta('Data/SPLC.txt')
main = data[0]
introns = data[1:]
codons = get_codon_table('Data/DNA-codon-table.txt')

for i in introns:
    main = main.replace(i,'')

res = ''
for i in range(0, len(main),3):
    res += codons[main[i:i + 3]]

print(res.rstrip('Stop'))