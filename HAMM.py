# Counting Point Mutations

s = 'CGAACTATCGGACCTCGTAGTCAAACGAGGGCTCAGTCTACTTTGCTGTCCTACTGATGAAGTCGCCGGCGCATTAGTACTCGAATGTTCCGCCTCGTATAGAGTAAGACACCTTGACACACCTCGGGTTACGTGTGGAACGTTGCACGCATGCGCTCGAAACTCGAGCCACCTTAGTGCGAAGTAGTATCGTACACACTGAAAACTGTCGTGAGTATTGTTTTGTTTTCGGGGTCGCACTTCTTACTAAGTGTTGATTTTTACCGCGACTTAGTGAACTCATGTGTATGGCTCAGGGAGTGAACTATAGAGGCATATATGGAACGGCCATTCGTAAAACCAGCACTGGGCTGTGAGTCGCCTTGCTCTCTCTAGTGTCGTATTATTCGATCAATTTCCAAGCGGGGTCGTTTTGTCCCTCACGGAGAAAGCTTTCAGCCCAATGTGGTATGGCGCAGCGGATTGCGCGCATTGGCACGTGATGAGTAAAAGGACGCTATCATGGGCCATCACTGGTAGACCACCGATACAAGGTAGGCACAGTTCCGTAGTATTTCAGTCCAACACGCGCATGCCCTCGTCCGTAGGGACTGAATTACTCTTCCAAATACATGGGTTGCGACTTCCTGCCCGACCTCGTGACCCCAATAAGTATCTTCCAAGATAATTACGCACGGCAATGGTGTCCTCTGAAGGGCCGTTCGGCCCTTAATGATTCCCCGGTCTTGTAAACCTAATCACCGTTGAATGTTATGCCGGGGGAAATACGTCCATCATGCCGCACATTAACCGGATTCGGTTATAGTTGGTTAAAGCAGGAATTGTGTGTGAGTAGTAATGGGTTGCGGCCATGCATATGTAACGTCCAGTGCTTATTCGTCTACGACTGTGTTATTGGTT'
t = 'CGTGTTAAATCAACTAGATTTGATACGCACGCAGACTCGAGTTACCCTTGACTGCACTTCAGGTGCCGCCTCTTTTGTCAAGGACTCCTCCCAAACATCTGGAGTACGACCCTAGAACTAGACCTTGGGCGCCGTATTAACGCTACCGGCGGTAGCTTTCTTGTCGCCCAAGCCGAGCGTGTCCCGAGTTGAAAAAAACAAAGAACCGGCATTATTAACGTTATCTATAAGAGGTCCCCCTCATCGCGGTATGACGGCCGCTTCCAGGGCTTGCTATAATTAACAGAATCGGTCGTGTAGGGGATTATGCAGGCGGAGACTGATCTGACATTTAAACGCTATGTGTACGGTTGTGAGTTGGGGTCCTATCAGACCAGGCATATCATTTAATAAATGTAGTACGCCTTTTGTTAGAATCCTCATGGAGAGATCTTCTAGGCCAATGTGGTGTGTAGAATCCGAATGCAAGGATGGCTACTAGAGTTGTTAGAGAACAGTGACATCCCAGGTATCAGGAAGGCCAGCTAGACCAAGTTGGACGAGTACGACAGGTAGCCGGACCTCCTCGCGACTTCACTGGTGCGATCGGGACACTTTGCTCTTTGAAATCCGGGCGCTTCCTCTTGCTGCTCGCCCTTGCAACCTCCTTTAGTCCGATTAAACTCAATAGCGCCTAGTAAGGTTCTCCGCCGTAAAGGCTAGCGCCTGCTAATGCAACCTCGGACATTTTTACCGATTTAGCGCTCCCCTTCACAACGGCGGAAAGACGTTTCCCTTTTCACACAACAGGCGGATTAGTTCCTCATCGAATGACGATTCAATAAGCTGAACGTCGGAATAATTGGCCTAAAGGCATGCTATATGCGTAAAGCTTAGGCCGCTATGCCTTTGTGCATGTAG'

# Hamming distance betwen s and t is count of places where letters don't match
res = sum([v != t[i] for i, v in enumerate(s)])
print(res)

