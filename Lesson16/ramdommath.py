# 1) Import the `random` module to generate random numbers.

# 2) Create a variable `playing = True` to control the game loop.

# 3) Generate a random number between 0 and 9 using `random.randint(0, 9)`

# and convert it to a string, then store it in `number`.

# (This is the secret number the user must guess.)

# 4) Print instructions explaining the guessing game.

# 5) Start a `while` loop that runs as long as `playing` is True:

# a) Take a guess from the user and store it in `guess`.

# 6) Check if the user's guess matches the secret number:

# a) If `number == guess`:

# i) Print a winning message.

# ii) Display the secret number.

# iii) Stop the loop using `break` (game ends).

# 7) Otherwise (if the guess is incorrect):

# a) Print a message telling the user to try again.

# b) The loop continues and asks for another guess.
import random
a=random.randint(0,9)
while True:
    n=int(input("Enter number"))
    if a==n:
        print("The numbers match")
        break
    else:
        print("Try again")