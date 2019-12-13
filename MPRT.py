# Finding a Protein Motif

from urllib.request import urlopen
file = open('Data/MPRT.txt')
sample = file.read()
protein_ids = sample.split('\n')

def get_protein(id):
    # print(pid)
    url = 'https://www.uniprot.org/uniprot/{}.fasta'.format(id)
    data = urlopen(url).read()
    body = data.decode('ascii')
    p = [i.replace('\n', '') for i in body.lstrip('>').split('\n', 1)][1]  # Read one entry FASTA format
    return p


result = {}
for pid in protein_ids:
    result[pid] = []
    p = get_protein(pid)
    pos = 0
    while True:
        pos = p.find('N', pos)
        if pos == -1 or pos >= (len(p) - 3):
            break;

        if p[pos+1] != 'P' and p[pos+3] != 'P' and (p[pos+2] == 'S' or p[pos+2] == 'T'):  # Verify match to 'N{P}[ST]{P}'
            result[pid].append(pos+1)
        pos += 1


for r in filter(lambda r: result[r], result):
    print(r)
    print(' '.join(str(i) for i in result[r]))