from random import randint, choice
from time import sleep


# Roadmap for reorganizing this file:
# 1. Keep one function per responsibility.
#    - get_word(difficulty): choose a word.
#    - get_valid_difficulty(): keep asking until the user enters 0-5.
#    - get_valid_guess(guessed_letters): keep asking until the user enters
#      one new alphabetic character.
#    - display_progress(secret_word, guessed_letters): show the current word
#      with underscores for missing letters.
#    - process_guess(secret_word, guessed_letters, guess, lives): update the
#      guessed letters and lives, then return a consistent result.
#    - has_won(secret_word, guessed_letters): return True only when every
#      letter in the secret word has been guessed.
#    - play_game(): run the full game loop.
#
# Pseudocode for the final flow:
# - Ask for difficulty until the input is valid.
# - Pick a word from the matching difficulty list.
# - Start with empty guessed letters and a fixed number of lives.
# - While the player still has lives and has not won:
#   - Show guessed letters.
#   - Show the masked version of the word.
#   - Ask for one valid guess.
#   - If the guess was already used, show a message and do not remove a life.
#   - If the guess is in the word, keep the same lives.
#   - If the guess is not in the word, remove one life.
#   - Check whether all letters in the word are now guessed.
# - Print either the win message or the lose message.
def get_word(difficulty:int):
    # Pseudocode:
    # - Store the difficulty dictionary.
    # - Read the list for the chosen difficulty.
    # - Pick one random word from that list.
    words = {
    0: ["cat", "sun", "ball", "tree", "fish", "book", "lamp"],
    1: ["garden", "winter", "planet", "silver", "bottle", "window"],
    2: ["keyboard", "journey", "mountain", "rhythm", "weather", "pyramid"],
    3: ["algorithm", "callback", "interface", "scenario", "velocity", "protocol"],
    4: ["encryption", "middleware", "asynchronous", "phenomenon", "metamorphosis"],
    5: ["idiosyncrasy", "onomatopoeia", "hieroglyphic", "sesquipedalian", "knickknack"]
}
    options = words[difficulty]
    return options[randint(0,len(options)-1)]

def get_valid_difficulty():
    choice = input('Enter a number from 0-5 to choose a difficulty\n- 0 for easy, 5 for difficult\nEnter here: ')
    if choice.isdigit() and 0 <= int(choice) <= 5:
        return int(choice)
    print("Invalid input. Please enter a number between 0 and 5.")
    return get_valid_difficulty()


def valid_guess(guessed_letters):
    letter = input('Enter your guess here: ').lower()
    if len(letter)!=1:
        print(f"Make sure to enter a valid input, only one letter")
        return valid_guess(guessed_letters)
    elif not letter.isalpha():
        print(f"Make sure to enter a valid input, only accepts letters")
        return valid_guess(guessed_letters)
    elif letter in guessed_letters:
        print(f"You have already tried {letter}! Try another one!")
        return valid_guess(guessed_letters)
    return letter
            
def display_progress(guessed, secret_word):
    [print('_ ', end='') if f not in guessed else print(f,end='') for f in secret_word]
    print(guessed.join(''))
    
def has_won(word, guessed):
    return all(f in guessed for f in word)
           
def update_game_state(secret_word, guess,guessed_letters, lives):
    guessed_letters.append(guess)

    if guess not in secret_word:
        lives-=1
        print(f"Sorry, '{guess}' is not there. Lives remaining: {lives}")
    else:
        print(f"Nice! '{guess}' is in the word.")
        print('')
    [print('_ ', end='') if f not in guessed_letters else print(f,end='') for f in secret_word]
    print('')
    print(f"\n\nGuessed letter are {guessed_letters}")
    return (guessed_letters, lives)




def play_game():

    print("Do you want to play yourself, or do you want the computer to play against itself.")
    print("If you want to play enter anything, if you want the computer to play, enter 1.")
    if input("Enter here: ")=='1':
        autoplay()
    else:
        difficulty = get_valid_difficulty()
        word = get_word(difficulty)
        lives = 5
        guessed_letters = []

        print("\n--- Game Start! ---")

        while lives > 0:
            # display_progress(word, guessed_letters)
            
            current_guess = valid_guess(guessed_letters)
            result = update_game_state(word,current_guess, guessed_letters, lives)
            guessed_letters, lives = result[0], result[1]
            if has_won(word, guessed_letters):
                print(f"\nCongratulations! You won! The word was: {word}")
                return 

        print(f"\nGame Over. You ran out of lives. The word was: {word}")
    print(f"If you want to play again enter 1, else enter anything:")
    if int(input("->"))==1:
        play_game()
    else:
        print('Thanks for playing')
        return
    
def autoplay():
    print("Starting Autoplay")
    difficulty = randint(0,5)
    word = get_word(difficulty)
    lives = 5
    letters = list("abcdefghijklmnopqrstuvwxyz")
    guessed_letters = []

    print("\n--- Game Start! ---")

    while lives > 0:
        sleep(1)
        current_guess = letters.pop(randint(0,len(letters)-1))
        result = update_game_state(word,current_guess, guessed_letters, lives)
        guessed_letters, lives = result[0], result[1]
        
        if has_won(word, guessed_letters):
            print(f"\nCongratulations! You won! The word was: {word}")
            return 
    print(f"\nGame Over. You ran out of lives. The word was: {word}")



if __name__ == "__main__":
    play_game()

        




