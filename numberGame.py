import random 
var = -1

print("The maximum number able to be generated is?")
read = int(input()) 
var = random.randint(0, read)

guess = None
count = 0

while guess != var:
    print("Guess a number")
    count += 1
    guess = int(input())
    if guess > var:
        print("The answer is lower")
    elif guess < var:
        print("The answer is higher")

print(f"You WON! It took {count} guesses")

