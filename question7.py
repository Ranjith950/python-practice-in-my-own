class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.emp_id=employee_id
        self.salary=salary
    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")
class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department):
        super().__init__(name,age,employee_id,salary)
        self.dep=department
    def display(self):
        super().display()
        print(f"Department: {self.dep}")
name=input("Enter the name:")
age=int(input("Enter age:"))
employee_id=int(input("Enter ID:"))
salary=int(input("Enter salary:"))
department=input("Enter department")
m=Manager(name,age,employee_id,salary,department)
m.display()
        