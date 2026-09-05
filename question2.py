class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print(f"Brand: {self.brand}")
        print(f" Model: {self.model}")
        print(f"Price: {self.price}")
brand=input("Enter the brand:")
model=input("Enter the mosdel:")
price=float(input("Enter the price:"))
c=Car(brand,model,price)
c.display()