import math
for col1 in range(1, 51):
    col2 = col1**2
    col3 = round(math.sqrt(col1),4)
    print(f"{col1}\t{col2}\t{col3}")