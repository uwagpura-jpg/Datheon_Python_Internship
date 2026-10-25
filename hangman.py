
import random

# Words available for the game
words = ["python", "docker", "server", "cloud", "linux"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = set()

# Maximum incorrect guesses
attempts_left = 6

# Hangman stages
hangman_art = [
    """
     +---+
     |   |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =======
    """
]

print("=" * 30)
print("       HANGMAN GAME")
print("=" * 30)

while attempts_left > 0:

    # Display the current word
    displayed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    print("\nWord:", displayed_word)
    print("Wrong attempts left:", attempts_left)
    print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "None")

    # Check whether the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! YOU WIN!")
        break

    # Take user input
    guess = input("\nGuess a letter: ").strip().lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one alphabet letter.")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts_left -= 1
        print("Wrong guess!")
    
    # Display the Hangman drawing
    mistakes = 6 - attempts_left
    print(hangman_art[mistakes])

# Final result
if not all(letter in guessed_letters for letter in secret_word):
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)
