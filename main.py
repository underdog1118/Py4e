score = input("Enter Score: ")
try:
    sco = float(score)
except:
	print("wrong input")
if sco > 1.0 or sco < 0.0:
    print("wrong score")
elif sco >= 0.9:
	print ("A")
elif sco >= 0.8:
    print ("B")
elif sco >= 0.7:
    print("C")
elif sco >= 0.6:
    print ("D")
else:
    print("F")
