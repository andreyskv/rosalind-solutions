# Ordering Strings of Varying Length Lexicographically

sample = 'K I Y G P S F L C D'
data = sample.replace(' ','')
N = 4
lex = ['']*N


def iterate(l, lex):

    if l >= N:
        return

    for s in data:
        lex[l] = s
        print(''.join(lex))
        iterate(l + 1, lex.copy())


iterate(0, lex)