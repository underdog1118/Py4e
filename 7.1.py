'''
Writer:UNDERDOG
Time:..
'''
# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
    f = fh.read()
except:
    print('wrong')
    quit()
for letter in f:
    letter = letter.rstrip()
    fh2 = f.upper()
print(fh2)