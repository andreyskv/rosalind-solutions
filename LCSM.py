# Finding a Shared Motif

import time
start_time = time.time()

nucleotides = ['A', 'C', 'G', 'T']

# Read FASTA format file
def read_fasta(filename):
    file = open(filename)
    sample = file.read()
    # Convert FASTA string into dictonary
    entries = dict(map(lambda e: [i.replace('\n', '') for i in e.split('\n', 1)][::-1], sample.lstrip('>').split('>')))
    return list(entries.keys())


dna_list = read_fasta('Data/LCSM.txt')
dna_list_length = len(dna_list)
# print(dna_list)

picks = nucleotides.copy()  # Start with 1 letter nucleotides as common string candidates
new_picks = ['']  # Initialize with not empty list
while new_picks:  # Search until the new candidates list has anything in it
    new_picks.clear()  # Reset new candidates list
    for p in picks:
        for n in nucleotides:
            new_p = p + n  # Append a nucleotide letter to form a new candidate
            if len([n for n in dna_list if new_p in n]) == len(dna_list):  # Check if new candidate passes test and contain in all strings
                new_picks.append(new_p)  # Store it
    if new_picks:  # Swap new candidates with candidates list. Candidates are now former new candidates.
        picks, new_picks = new_picks, picks
print(picks)

# Note: possibly a little shorter solution is to use a queue instead of tracking lists swaps on each layer for BFS
# Performance turns out to be identical for both methods
# Queue method
# pick = ''
# q = deque(nucleotides.copy())
# while q:
#     pick = q.popleft()
#     for n in nucleotides:
#         new_p = pick + n
#         if len([n for n in dna_list if new_p in n]) == len(dna_list):
#             q.append(new_p)
# print(pick)

print("time elapsed: {:.2f}s".format(time.time() - start_time))