n=int(input("Enter your number"))
sum=0
for i in range(0,n):
    for j in range(0,i+1):
        sum=sum+1
        print(sum,end=" ")
    print()
    