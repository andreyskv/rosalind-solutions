# Maximum Matchings and RNA Secondary Structures
import math

s = 'UCUUGCUUGACAUAUCUUAUAUAUAAAGCUCACGAGGCUAAAAGAUGUGGUAAACAAGAGAUGCUGCUUAGCCGCUCCCAAAGCAAUCUAACG'
# s = 'AUGCUUC'

A, U, C, G = s.count('A'), s.count('U'), s.count('C'), s.count('G')
print(A, U, C, G)

au = math.perm(max(A, U), min(A,U))
cg = math.perm(max(C,G), min(C,G))
print(au*cg)

