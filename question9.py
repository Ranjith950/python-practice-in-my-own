class Shape:
    def area(self):
        print("")

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return f"Area: {self.length*self.width}"
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return f"Area: {self.radius*self.radius*3.14}"
length=int(input("Enter the length:"))
width=int(input("Enter the width:"))
radius=int(input("Enter the radius:"))
choice=int(input("Enter 1 for Rectangle,2 for Circle:"))
res={1:Rectangle(length,width),2:Circle(radius)}
if choice in res:
    c=res[choice]
    print(c.area())
else:
    print("Invalid Choice")
