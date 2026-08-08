n=int(input("Enter the number"))
a=True
for i in range(2,n):
    if n%i==0:
        a=False
        break
if a==True:
    print("It is a prime number")
else:
    print("It is not a prime number")
