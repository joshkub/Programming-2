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
    per1 = round(group1/value * 100, 2)
    per2 = round(group2/value * 100, 2)
    per3 = round(group3/value * 100, 2)
    per4 = round(group4/value * 100, 2)
    per5 = round(group5/value * 100, 2)
print (f"     Age Group\t Distribution\tPercentage\n\t <20\t\t{group1}\t{per1}\n\t 20-39\t\t{group2}\t{per2}\n\t 40-59\t\t{group3}\t{per3}\n\t 60-79\t\t{group4}\t{per4}\n\t >79\t\t{group5}\t{per5}")