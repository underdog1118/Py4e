'''
Writer:UNDERDOG
Time:..
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
l = list()
bigname = None
bigcount = None
for line in handle:
    line = line.rstrip()
    A = line.split()
    if line.startswith('From') and len(A)>2:
        a = A[1]
        l.append(a)
    else:
        continue
for aaa in l:
    d[aaa] = d.get(aaa,0) + 1
for c,e in d.items():
    if bigcount ==  None or e > bigcount:
        bigcount = e
        bigname = c
print(l)
print(d)
print(bigname,bigcount)
