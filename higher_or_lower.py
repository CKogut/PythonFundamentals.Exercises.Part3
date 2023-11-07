from random import randrange

def guess():
    return int (input("Enter a number between 0 and 10: "))

def random_num():
    return randrange(10)

def high_or_low(guess, target):
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("You guessed it!")

rand = random_num()
high_or_low(guess(), rand)
print("The number was " + str(rand))