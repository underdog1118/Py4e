'''
Writer:UNDERDOG
Time:..
'''
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
a = 0
b = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    a = a + float(line[19:])
    b = b + 1
c = float(a/b)
print('Average spam confidence: ',c)


