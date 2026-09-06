class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class Student(Person):
    def __init__(self,name,age,roll_num,marks):
        super().__init__(name,age)
        self.roll_num=roll_num
        self.marks=marks
    def display_student(self):
        super().display_person()
        print(f"Roll Number: {self.roll_num}")
        print(f"Marks: {self.marks}")
name=input("Enter name:")
age=int(input("Enter age:"))
roll_number=int(input("Enter roll_number:"))
marks=int(input("Enter marks:"))
s=Student(name,age,roll_number,marks)
s.display_student()