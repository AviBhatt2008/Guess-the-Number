import random

chancesLeft = 5
num = random.randint(1, 50)
won = ""

## print(num)

print("I am thinking of a number from 1-50 (which could also be 1 or 50).")
print("You have 5 chances to guess the number.")

while chancesLeft > 0:
    guess = int(input("Guess the number I am thinking of: "))
    
    if guess < num:
        chancesLeft -= 1
        print("Your guess is too low. You have {0} chances remaining.".format(chancesLeft))
    if guess > num:
        chancesLeft -=1
        print("Your guess is too high. You have {0} chances remaining.".format(chancesLeft))
    if guess == num:
        chancesLeft -= 1
        print("Your guess is correct - You Win!")
        attempts = 5-chancesLeft
        print("You guessed the number {0} after {1} attempts".format(num, attempts))
        won = "true"
        break

if(won != "true"):
    print("This means you lose as the number was {0} - better luck next time".format(num))

