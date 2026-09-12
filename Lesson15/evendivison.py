while True:
    try:
        a=int(input("Ente number "))
        if a%2==0:
            print("This is an even number")
            break
    except ValueError:
        print("This is not a number")