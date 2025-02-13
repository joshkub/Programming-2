import random
playernum = int(input("Enter a # between 1 & 20:"))
computernum = random.randint(1, 20)
print ("Computer's Number: " + str(computernum))
print ("Player's Number: " + str(playernum))
if playernum == computernum:
    print ("You Won!")
else:
    print ("Better luck next time.")