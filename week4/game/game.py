import random

while True:
    Level=input("Level: ")
    if Level.isdigit() and int(Level)>0 :
        level=int(Level)
        break
    else:
        print("Please enter positive integer other than 0")

target=random.randint(1, level)
while True:

    guess_input = input("Guess: ")
    if guess_input.isdigit() and int(guess_input)>0 :

       guess=int(guess_input)
    else:
       print("Please enter positive integer other than 0")


       continue
    if guess<target:

       print("Too small!")
    elif guess>target:
        print("Too large!")
    else:
        print("Just right!")
        break





