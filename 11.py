'''
Writer:UNDERDOG
Time:..
'''
import re
x = 'From abc@uct.a sat jan 05'
y = re.findall('@(\S*)',x)
print(y)