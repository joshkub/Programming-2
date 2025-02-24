import math
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
Product = a * b
AwesomeSauce = math.lcm(a, b)
GCD = Product / AwesomeSauce
print(f"GCD : {GCD}")