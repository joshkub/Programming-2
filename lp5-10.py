num1 = int(input("Enter # of dozen to be purchased: "))
num2 = int(input("Enter # of dozen to be purchased: "))
while num2 > 0:
    temp = num1 % num2
    num1 = num2
    num2 = temp
print (temp)