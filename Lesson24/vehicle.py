class Vehicle:
    def __init__(self,price,model):
        self.price=price
        self.model=model
    def display(self):
        print(f"The price is {self.price} and model is {self.model} ")

a=Vehicle(2000,"M1")
print(a.price)
print(a.model)

b=Vehicle(50000,"M5")
print(b.price)
print(b.model)
a.display()
b.display()