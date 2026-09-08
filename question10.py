class Employee:
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self,monthly_salary):
        self.monthly_salary=monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self,hours_work,hours_rate):
    
        self.hours_w=hours_work
        self.hours_r=hours_rate
    def calculate_salary(self):
        return self.hours_w * self.hours_r

class Intern(Employee):
    def __init__(self,stipend):

        self.stipend=stipend
    def calculate_salary(self):
        return self.stipend

monthly_salary=int(input("Enter the salary:"))
hours_work=int(input("Enter the hours:"))
hours_rate=int(input("Enter the rate:"))
stipend=int(input("Enter the stipend:"))
i=Intern(stipend)
print(i.calculate_salary())