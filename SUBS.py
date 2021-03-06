# Finding a Motif in DNA

sample = 'TGAGTTCTATACACTGGCAGTTCTAGCTGACAGTTCTAAGTTCTAAAGAGTTCTAAGTTCTAGGTGAAGTTCTACAGTTCTAAGTTCTAAGTTCTACATGAGTTCTATCAGTTCTATTTAGTTCTAGCCAGTTCTAAGTTCTATGCAGTTCTAGAGTTCTACTCCTGAGTTCTACAGTTCTAAGTTCTAGGAAGTTCTAAAGTTCTACAGTTCTAATGCAAGGCAGTTCTAAGTTCTACTTAGTTCTAAGGCCCAAGTTCTACAGTTCTACAGTTCTAAGTTCTATCGAAGTTCTACGAAAAGTTCTAGTCAGTTCTATTCGCTTGGGGAGTTCTAGAACCAGTTCTAAACAGTTCTACAGTTCTAACAGTTCTATGTGTATCTAGTTCTATAACAGTTCTACAGTTCTAGCAGTTCTAGGAGTTCTATGGCTGTACTCAGTTCTAAGAATAGTTCTAAAATCGAAAGTTCTAATGTTCGAAGTTCTATTTAAGTTCTATAGTTCTAAGTTCTAGAGTTCTAGAGTTCTAGCTCTCACGTAAGTTCTATGGTGAAGTTCTAGATAGTTCTAGGTAATACACCCCAGTTCTAAGCTTATAGTTCTAACTCGGAGTTCTAACTGAGTCTTAGTTCTACAGGAGTTCTATCTAAGTTCTAAGATATTATGTAGTTCTAGTAGTTCTAAGTTCTATAAGTTCTATGAGTTCTAAGTTCTACAGTTCTAACAGTTCTAGTGAGTTCTAAAAGCCCACAAGTTCTAAGTTCTAAGTTCTATCAGTTCTATCAGTTCTAAATCTAGTTCTAGGAGTTCTACGGTGGCAGGAGTTCTAGCAGAGTTCTAAGTTCTAGCAGTTCTAGATCGTCGAACCAGTTCTAAGTTCTATAGTTCTACCTTTAGTTCTAAAAGTTCTACCCGCAGTTCTATCTCGTTGTAGTTCTAAAGTTCTATTAAAGTTCTAATAGTTCTAAGC'
motif = 'AGTTCTAAG'

positions = [];
i = 0
while i >= 0:
    i = sample.find(motif, i)
    if i > 0:
        i += 1;
        positions.append(i)

print(' '.join(str(x) for x in positions))