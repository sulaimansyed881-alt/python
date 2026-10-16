import random
letter=["abc","efg","hij","lmn"]
n1=random.choice(letter)
n2=random.randint(0,100)
a=str(n2)
b=n1+a
print("The password is",b)
