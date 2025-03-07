class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self._area = 0
        self._perim = 0
    def calculate(self):
        self._area =  self.length + self.width
        self._perim = 2 * self.length + 2 * self.width
    
    def get_area(self):
        return self._area
    
    def get_perimeter(self):
        return self._perim
    
def main():
    length = int(input("Emter length: "))
    width = int(input("Enter Width: "))
    shape =  Shape(length, width)
    shape.calculate()
    print("Area:", shape.get_area())
    print("Perimeter:", shape.get_perimeter())
    pass

if __name__ == "__main__":
    main()
    
        