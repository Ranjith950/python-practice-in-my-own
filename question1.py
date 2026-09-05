class Student:
  def __init__(self,name,age,marks):
    self.name=name
    self.age=age
    self.marks=marks
  def display(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Marks: {self.marks}")
name=input("Enter name:")
age=int(input("Enter age:"))
marks=float(input("Enter marks:"))

st=Student(name,age,marks)
st.display()