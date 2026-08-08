amount=int(input("Enter the amount you want to withdraw"))
a=amount//100
amount=amount%100
b=amount//50
amount=amount%50
c=amount//10
print("The number of required 100Rs notes is",a)
print("The number of required 50Rs notes is",b)
print("The number of required 10Rs notes is",c)
