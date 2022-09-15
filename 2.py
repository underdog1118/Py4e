'''
Writer:UNDERDOG
Time:..
'''
def computepay(h,r):
    x = h*r
    return x

hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Bad input")
if  h <= 40.0:
	p = computepay(h,r)
	print("Pay",p)
else:
    p = computepay(40,r)+computepay((h-40),1.5*r)
    print("Pay",p)