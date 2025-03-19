people = [17, 80, 79, 60, 21, 20, 1, 39, 40, 59, 61, 4, 16, 47, 52, 35, 54, 85, 21, 15, 48, 49, 50]
value = 0
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
for i in people:
    if i > 79:
        value += 1
        group1 += 1
    if i >= 60 and i <= 79:
        value += 1
        group2 += 1
    if i >= 40 and i <= 59:
        value += 1
        group3 += 1
    if i >= 20 and i <= 39:
        value += 1
        group4 += 1
    if i < 20:
        value += 1
        group5 += 1


    

print ()