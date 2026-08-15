import random

play = True

while play:
    try:
        min_num = int(input("Min: "))
        max_num = int(input("Max: "))
    except ValueError:
        print("Please enter integer values for Min and Max.")
        continue

    if min_num > max_num:
        print("The minimum number cannot be greater than the maximum number. Please try again.")
        continue

    target = random.randint(min_num, max_num)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Please enter an integer.")
            continue

        if guess == target:
            print("Correct!")
            break
        if guess < target:
            print("Bigger!")
        else:
            print("Smaller!")

        abs_diffrence = abs(guess - target)
        if abs_diffrence <= 10:
            print("Hot")
        elif abs_diffrence <= 30:
            print("Warm")
        else:
            print("Cold")

    answer = input("Try again? (yes/no): ")
    while answer != "yes" and answer != "no":
        print("Please type 'yes' or 'no'.")
        answer = input("Try again? (yes/no): ")
    if answer == "no":
        play = False
    else:
        print("Here we go again")
    if answer == "yes":
        play = True