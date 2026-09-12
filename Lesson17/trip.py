print("We are a trip planners")
print("We have 4 places, Paris for $400 ,France $600 , Europe$500 and England $900")
a=int(input("Enter 1 for Paris, 2 for France, 3 for Europe and 4 for England"))
total=0
if a==1:
    print("You have chosen paris")
    total=total+400
elif a==2:
    print("You chose france")
    total=total+600
elif a==3:
    print("You chose europe")
    total=total+500
elif a==4:
    print("You chose england")
    total=total+900
else:
    print("Choose from above options")
print("How many days are you staying,for 1 day it is $100,2 days is $300, for 3 days is $400")
n=int(input("Enter number of days you are staying"))
if n==1:
    print("You are staying for 1 day")
    total=total+100
elif n==2:
    print("You are staying for 2 days ")
    total=total+300
elif n==3:
    print("You are staying for 3 days ")
    total=total+400
else:
    print("Choose from above options")
print("The total cost is",total)


