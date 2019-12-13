# Read FASTA format file
gc_file = open("Data/GC.txt")
gc_sample = gc_file.read()

# Convert FASTA string into dictonary
entries = dict(map(lambda e:[i.replace('\n','') for i in e.split('\n',1)], gc_sample.lstrip('>').split('>')))

# Find percentage of C and G letters in the string
gc_content = {}
for k in entries.keys():
    cnt = 100*(entries[k].count('C') + entries[k].count('G'))/len(entries[k])
    gc_content[k] = cnt

# Get maximum value
maxValueKey = max(gc_content, key=gc_content.get)
print(maxValueKey)
print(round(gc_content[maxValueKey], 6))