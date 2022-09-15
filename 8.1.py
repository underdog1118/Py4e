x'''
Writer:UNDERDOG
Time:..
'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    b = line.rstrip()
    c = b.split()
    for letter in c:
        if letter not in lst:
            lst.append(letter)
        else:
            continue
lst.sort()
print(lst)


