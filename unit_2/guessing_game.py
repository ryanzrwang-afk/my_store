import random

play = True

while play:
    min_num = int(input("Min: "))
    max_num = int(input("Max: "))

    if min_num > max_num:
        min_num, max_num = max_num, min_num

    secret = random.randint(min_num, max_num)

    while True:
        guess = int(input("Guess: "))

        if guess == secret:
            print("Correct!")
            break
        elif guess < secret:
            print("Bigger!")
        else:
            print("Smaller!")

    if input("Try again? (yes/no): ").strip().lower() != "yes":
        play = False