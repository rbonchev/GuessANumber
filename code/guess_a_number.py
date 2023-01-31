import random

computer_number = random.randint(1, 100)

attempts = 10

for attempt in range(10):
    player_input = input("Guess the number between 1 and 100: ")
    attempts -= 1
    print(f"Attempts left: {attempts}")

    if not player_input.isdigit():
        print("Invalid Input. Please enter a number!")
        continue

    player_input = int(player_input)

    if player_input == computer_number:
        print(f"You guessed it!")
        break

    if player_input > computer_number:
        print("Number is too high!")
    elif player_input < computer_number:
        print("Number is too low!")

play_again_input = input("Type [yes] if you want to play again or [no] to quit: ")

if play_again_input == "yes":
    exec(open("guess_a_number.py").read())
else:
    print("Thank you for playing!")
