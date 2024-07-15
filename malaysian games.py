import random

# List of popular traditional games in Malaysia
traditional_games = ["Congkak", "Sepak Takraw", "Wau", "Gasing", "Batu Seremban"]

# Randomly select a game
selected_game = random.choice(traditional_games)

# Instructions for the player
print("Guess the popular traditional game in Malaysia!")

# Initialize the number of attempts
attempts = 3

while attempts > 0:
    guess = input("Enter your guess: ")
    if guess == selected_game:
        print("Congratulations! You guessed it right!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong guess! You have {attempts} attempts left. Try again.")
        else:
            print(f"Sorry, you've run out of attempts! The correct answer was '{selected_game}'.")

print("Game Over")

