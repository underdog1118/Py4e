'''
Writer:UNDERDOG
Time:..
'''
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        x = int(num)
    except:
        print("Invalid input")
        continue
    for value in [x]:
        if largest is None:      #aka --- if largest is None or value > largest:
            largest = value      #          largest = value
        elif value > largest:
            largest = value
    for value2 in [x]:
        if smallest is None:
            smallest = value2
        elif value2 < smallest:
            smallest = value2
print("Maximum is", largest)
print("Minimum is", smallest)