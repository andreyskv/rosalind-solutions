# Read FASTA format file
def read_fasta(filename):
    file = open(filename)
    sample = file.read()
    # Convert FASTA string into dictonary
    entries = dict(map(lambda e: [i.replace('\n', '') for i in e.split('\n', 1)][::-1], sample.lstrip('>').split('>')))
    return list(entries.keys())


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