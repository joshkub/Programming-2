class solve:
    def __init__(self):
        self.all = []
        self.total = 0
        self.group1 = 0
        self.group2 = 0
        self.group3 = 0
        self.group4 = 0
        self.group5 = 0
        self.per1 = 0
        self.per2 = 0
        self.per3 = 0
        self.per4 = 0
        self.per5 = 0

        with open("programs/Langdat/prog213e.txt", 'r') as f:
            for line in f:
                self.all.append(int(line))
    def calc(self):
        for x in self.all:
            if x in range(0,19):
                self.total += 1
                self.group1 += 1
            if x in range(20,39):
                self.total += 1
                self.group2 += 1
            if x in range(40,59):
                self.total += 1
                self.group3 += 1
            if x in range(60,79):
                self.total += 1
                self.group4 += 1
            if x in range(79,):
                self.total += 1
                self.group5 += 1
        self.per1 = round(self.group1/self.total * 100, 2) 
        self.per2 = round(self.group2/self.total * 100, 2) 
        self.per3 = round(self.group3/self.total * 100, 2) 
        self.per4 = round(self.group4/self.total * 100, 2) 
        self.per5 = round(self.group5/self.total * 100, 2) 
        print()
        
def main():
    c = solve()
    c.calc()
if __name__ == '__main__':
    main()


   

    