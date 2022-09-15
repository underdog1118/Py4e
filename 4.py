'''
Writer:UNDERDOG
Time:..
'''
def thing(a,b,c,d,e):
    l = -1
    for i in [a,b,c,d,e]:
        if i > l:
            l = i
    return l
x = thing(1123,2,3123114,4,5)
print(x)