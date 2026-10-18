class vehicle:

    def __init__(self,name,max_speed,price):
        self.name= name
        self.max_speed= max_speed
        self.price= price

class car(vehicle):
    pass

Sports_car = car("Ford Explorer",210,500000)
print("Vehicle name is",Sports_car.name)
print("Vehicle max speed is",Sports_car.max_speed)
print("Vehicle price is",Sports_car.price)
    