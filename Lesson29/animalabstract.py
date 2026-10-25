from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("I have 2 legs")
class snake(Animal):
    def move(self):
        print("I have no legs")
class dog(Animal):
    def move(self):
        print("I have 4 legs")
class lion(Animal):
    def move(self):
        print("I have 4 legs")
R = human()
R.move()
K = snake()
K.move()
L = dog()
L.move()
M = lion()
M.move()

