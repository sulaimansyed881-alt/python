class number1():

    privatevar = 90;
    def __privMeth(self):
        print("I am going to be number1")

    def hello(self):
        print("This is private")
m = number1()
m.hello()
m.__privMeth()


