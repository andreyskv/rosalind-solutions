# Calculating Expected Offspring

# EV formula; EV = sum( i*Pk for i in outcomes);

sample= '17617 18611 18650 18625 16316 18865'
N = 2

# Set outcome probabilities for a dominant allele offspring
P = {'AA-AA': 1, 'AA-Aa': 1, 'AA-aa': 1, 'Aa-Aa': 0.75, 'Aa-aa': 0.5, 'aa-aa': 0}

Pl = list(P.values())

Sl = [int(x) for x in sample.split(' ')]
EV = N*sum([s*p for s, p in zip(Sl, Pl)]);

print(EV)



