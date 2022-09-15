'''
Writer:UNDERDOG
Time:..
'''
import re
name = input("Enter file:")
handle = open(name)
y = list()
a = 0
x = list()
for line in handle:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    for w in y:
        if w != None:
            x.append(w)
print(x)

for word in x:
    b = int(word)
    a = a + b
print(a)