# Transcribing DNA into RNA
sample = 'ACGACAGCTCGATGTCAGGATTTGGCGAATGCGTATTTAAGAAAACGATACGAGGTAATCGTCGTTGTATACAAGGTCCGACCTGAGCGGTCACTCGTAGTGTCCGTTTTAGTTTGCAGTTTACAATAAGAATCCCACCCTCTCCTGCTGCGCTAGTGAAGCCAGGAGTCCGTCCAACGTAGATTTAGCTTTTGACGCCAACTGGCGTGACTCATGTCTATGCATGGACTAGTAGTACGTTTTGCAGTACTCTGCGGGCGTTTTAGACCCATATCGTCCGTAAGATTGCGCCTTACAACGCCCATGAAGACTCTCAGACCGGAGCGATGCGACGCCGGGCCTTATGATCAACGGAACTCTAACCCGATCACGGCGCTTTATCGTGGGAGAGTACTACAAATAGGCAAACACTAAGAATTCCTTCGCACAATCTGCAGGGACTGCAGTTGTCGATAATCCGAAATATCACGACCGCTGGCCTAGGCCTGGCATGGTGGACTTCCGATTCTGCATCGACTAGAATGACCAAAGGGAACTCCCTAAACATGACACCTTGGTGCGACATACCGGAATGTTAGCCAACTTTACCAGCCGACGACATATCAGATGTGAACCCCTCCCTTGTGAAAGGACACAGTACTCTGCGATGTTCCTGTTTCCCAATTTATATTTGCGCTTATTCCTCTGTACCATGGCTAATCTAATCTTTCTAGCGACGAGTGAATAGGATCTCTCCTTGTGATAATCTACCTATAACAACTGGCTTGAAGACCTGGGTCGAATTCAAGAGGGCTAAAATTGTTTGATATCGAGCCAATACTACTATTGATAGCTGACGAGGTTTGGACGTGGGACATAGAGCCGTATTTCTTCCTTACCAGCCTGAGTCGACGCAAACACGCTCGGCGAGCATAGCGCCCGATT'

nt = ['A', 'C', 'G', 'T', 'U']
result = sample.replace(nt[3], nt[4])
print('Result:\n', result)
