# Speeding Up Motif Finding
# Fantastic explanation of KMP algorithm https://www.youtube.com/watch?v=GTJr8OvyEVQ

file = open('Data/KMP.txt')
sample = file.read()
entries = dict(map(lambda e: [i.replace('\n', '') for i in e.split('\n', 1)][::-1], sample.lstrip('>').split('>')))
s = list(entries.keys())[0]

# s = 'CAGCATGGTATCACAGCAGAG'
N = len(s)
kmp = [0]*N

i = 1; j = 0
while i < N:
    if s[i] == s[j]:
        kmp[i] = j + 1
        i += 1
        j += 1
    elif j == 0:
        i += 1
    else:
        j = kmp[j-1]

print(' '.join(str(x) for x in kmp))
