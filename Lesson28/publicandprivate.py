class myclass:

    __privateVar= 27
    def privMeth(self):
        print("I am inside myClass")

    def hello(self):
        print("Private Variable vALUE:", myclass.__privateVar)

foo = myclass()
foo.hello()
foo.privMeth()
