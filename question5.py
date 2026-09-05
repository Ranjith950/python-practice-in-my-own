class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self,update_marks):
        if update_marks<0 or update_marks>100:
            print("Invalid marks")
        else:
            self.__marks=update_marks
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
name=input("Enter name:")
marks=int(input("Enter the marks:"))
update_marks=int(input("Enter the update marks:"))
s=Student(name,marks)
s.marks=update_marks
s.display()