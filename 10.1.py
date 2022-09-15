'''
Writer:UNDERDOG
Time:..
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
lst2 = list()
lst3 = list()
dic = dict()
for line in handle:
    line = line.rstrip()
    A = line.split()
    if line.startswith('From') and len(A)>2:
        a = A[5]
        B = a.split(':')
        b = B[0]
        lst.append(b)
print(lst)
for key in lst:
   dic[key] = dic.get(key,0)+1
print(dic)
for k,v in dic.items():                 #for k,v in sorted(dic.items()):
    lst3.append((k,v))
lst3 = sorted(lst3,reverse=False)
for k,v in lst3:
    print(k,v)                          #print(k,v)




