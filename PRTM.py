# Calculating protein mass
sample = 'SKADYEK'


# Read mass table file
def get_mass_table(filename):
    mass_table_file = open(filename)
    mass_table = mass_table_file.read()
    d = dict(map(lambda e:  e.split(), mass_table.split('\n')))
    return dict([key,float(value)]  for key, value in d.items())


mt = get_mass_table('Data/Monoisotic-mass-table.txt')
print(mt)

res = round(sum(mt[x] for x in sample), 3)
print(res)
