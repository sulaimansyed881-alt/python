try:
    i=int(input("Enter the number"))
    print(i)
except ValueError:
    print("This is not a number")
finally:
    print("It is a sunny day")
    