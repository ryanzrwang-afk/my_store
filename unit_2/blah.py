import random

play = True

while play:
    min_num = int(input("Min: "))
    max_num = int(input("Max: "))

    secret = random.randint(min_num, max_num)
    guess = int(input("Guess: "))

    if guess == secret:
        print("Correct!")
        if input("Try again? (yes/no): ") != "yes":
            play = False
    elif guess < secret:
        print("Bigger!")
    else:
        print("Smaller!")