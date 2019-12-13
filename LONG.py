# Genome Assembly as Shortest Superstring

# Read FASTA format file
file = open("Data/LONG.txt")
sample = file.read()
# Convert FASTA string into dictonary
entries = dict(map(lambda e: [i.replace('\n', '') for i in e.split('\n', 1)][::-1], sample.lstrip('>').split('>')))
dna_list = list(entries.keys())


# Find overlap of two strings on both sides and combine strings the shortest way
def merge(s1, s2):
    res = ''
    for i in reversed(range(len(s1))):
        if s1[-i:] == s2[:i]:
            res = s1 + s2[i:]
            break
        elif s2[-i:] == s1[:i]:
            res = s2 + s1[i:]
            break
    return res


master_str = dna_list.pop()
while len(dna_list) > 0:
    tests = {merge(master_str, s1): s1 for s1 in dna_list}  # Return dictionary with key: overlap string, value: second string
    master_str = min(list(filter(lambda x: x != '', tests.keys())), key=len)  # Minimum legth key and exclude empty keys
    dna_list.remove(tests[master_str])  # Remove the string which was appended to the master string

print(master_str)
