def shutdown(n):
    if n=="Yes":
        print("Shutting down")
    elif n=="No":
        print("Abort shutdown")
    else:
        print("Not defined")
n=input("Enter Yes or No")
shutdown(n)
