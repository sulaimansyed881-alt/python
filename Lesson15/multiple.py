try:
    a=int(input("Enter numerator"))
    b=int(input("Enter denominator"))
    print("The division of a and b is",a/b)
except ZeroDivisionError:
    print("The denominator is not zero")
except ValueError:
    print("This is only for numbers")
except:
    print("There can be some exceptions")
    