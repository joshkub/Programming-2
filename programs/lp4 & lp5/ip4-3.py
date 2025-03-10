eggs = int(input("Enter # of dozen to be purchased: "))
dozen = eggs / 12
price = 0.0

# if dozen > 0 and dozen <= 99:
if 0 < dozen < 4:
    price = 0.50
elif 4 <= dozen < 6:
    price = 0.45
elif 6 <= dozen < 11:
    price = 0.40
elif dozen >= 11:
    price = 0.35
else:
    print("The # of dozen is invalid!")
    quit()

print("# of eggs is: " + str(eggs))
print("The total cost is: $" + str(price * dozen))