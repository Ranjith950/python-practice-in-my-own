class Rectangle:
    def __init__(self,length,width):
        self.len=length
        self.wi=width
    def area(self):
        return self.len*self.wi
    def display(self):
        print(f"Length: {self.len}")
        print(f"Breadth: {self.wi}")
        print(f"Area: {self.area()}")
length=int(input("Enter length:"))
width=int(input("Enter width:"))
r=Rectangle(length,width)
r.display()