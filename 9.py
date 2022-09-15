'''
Writer:UNDERDOG
Time:..
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    line = line.rstrip()
    A = line.split()
    for a in A:

        if a in d:
            d[a] = d[a]+1
        else:
            d[a] = 1

print(d)