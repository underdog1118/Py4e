'''
Writer:UNDERDOG
Time:..
'''
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()
lst2 = list()
for line in fh:
    line = line.rstrip()
    a = line.split()
    if line.startswith('From')  and len(a)>2:
        c = a[1]
        lst.append(c)
    else:
        continue
for letter in lst:
    if letter not in lst2:
        lst2.append(letter)
        count = count + 1
print(lst2)


print("There were", count, "lines in the file with From as the first word")