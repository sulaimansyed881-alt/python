class Person():

    def __init__(self,name,idnumber):
        self.name= name
        self.idnumber= idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
class Employee(Person):
    def __init__(self,name,idnumber,fees,position):
        self.fees= fees
        self.position= position

        Person. __init__(self,name,idnumber)
a= Employee("Mohan",1446,7800,"Office worker")
a.display()

