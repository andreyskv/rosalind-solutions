# Enumerating k-mers Lexicographically

sample = 'A B C D E F'
data = sample.replace(' ','')
N = 3
lex = [None]*N


def iterate(l):

    if l >= N:  # Once reached N the string is complete. Exit.
        print(''.join(lex))
        return

    # We are setting every position in 'lex' with every possible letter from data
    for s in data:
        lex[l] = s
        iterate(l + 1)


iterate(0)