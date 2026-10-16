import random
def intro(x):
    n=input("Enter your name")
    print(n)
    print("Welcome, we will play a game, guess a no. from 1 to 100")
    if x%2==0:
        print("Hint: This is even no.")
    else:
        print("Hint: This is odd no.")
def guess(x):

    while True:
        b=int(input("Guess no."))
        if b==x:
            print("This is correct")
            
            break
        elif b>x:
            print("The no. is too high")
        elif b<x:
            print("The no. is too low")
        else:
            print("Try again")
while True:
    x=random.randint(1,100)


    intro(x)
    guess(x)
    print("Do you wnat to play again")
    y=input("Enter Yes for yes enter No for no")
    if y=="No":
        print("Thank you")
        break
