def weather(n):

    if n<=0:
        return 0
    print("The weather is hot")
    weather(n-1)
weather(7)