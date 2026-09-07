class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog can shouting Bow Bow")
class Cat(Animal):
    def sound(self):
        print("Cat can shouting Meow Meow")
choice=int(input("Enter 1 for dog,2 for cat"))
d=Dog()
c=Cat()
if choice==1:
    d.sound()
elif choice==2:
    c.sound()
else:
    print("Invalid choice")
