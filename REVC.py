# Complementing a Strand of DNA
sample = 'AGGCGATAACGACACCAACCTTGCAAACGATGATGTTGAAAGGCGGGATCACCCTTATCGCGTTCTAATGGGTCGGTATCACGTTAAAAGGTAGGCATTGAGCAAGCAACGCTCCATCCACAACTTTTGTGGCTCACGAACTTGTTATGAATAATGTGACCTGGAAAGATTAGCGGCAGAATAAACCAACAGCGAGTTGTTAGGCCAGCACAATTGAAATCCGGAAAGTCAACTATACGTCCCAGCCTCCGATCCCCATCTTGCGGGTTATAAAACTGTATTGGACCTGAGAATTCGGTACGGTAGTCCGGTTGTAAATTGTTCGTCCAAATTGTTCAGGTTTAGCTTTGTGTAGGAGGCTCCACCGGGCGTTACGATTACATCCTTGTGTCCGCTGATTCGCCGACTTGTCACCCCCGTGGCTTGCTGATCATGTGCAGTTACGGGGATAGACGTCGTCCTATTTGATTAGACACTTCCTGTTTAGACAATTATAGCTAACCGCTGACATATTACCATATTCTTCGAGGTTTCGATAAAGTGTAGCACGTGGAAAATACCACGGCCACTCTGTTCCCGCACTTATACATCCTGCGGACAGGGAACTGTCTATAATTGGATGGCTAAAGTCCTGCGAGCGGACGTTTGCATGGTTCTGGAAACGCACGGATCACACATCTGTGTACCCGACAGGTCTTCGCTCCGGATCATGATTACTGCCCTATGTCTTGCATGAGACCCAGAAAGCGTCCCGCGAAATTAGGCTCTGTTGAGCCCATATACGGTCCGCAGCTAATTGACACACCTAACACATGCGCGTCCGTTTTGGTATGACTGCTTAAAGGACTCTCGCGTGAGCGCGCCCGCTACGGTTCTCGGCCTAG'

nt = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
result = ''
for n in sample[::-1]:
    result += nt[n]

print('Result:\n', result)
