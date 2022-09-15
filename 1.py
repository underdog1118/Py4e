'''
Zhengpeng Qiu  CS5001-22Fall  Lab02-problem_01
'''

def main():
   total_bill = float(input("How much is the total amount of the bill? "))
   tip_percentage = float(input("The percentage you will to tip(between 0 and 1): "))
   people_number = int(input("How many people are in the group? "))

   splitted_bill = total_bill*(1+tip_percentage)/people_number
   print("The amount for every person is : "+str(splitted_bill))

if __name__ == "__main__":
    main()