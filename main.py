from random import randint

def update_game_state(secret_word, guessed_letters,guess, lives):
    if guess not in guessed_letters:
        guessed_letters += guess
    else:
        print('Already guessed this letter\n')
    print(f'The guessed letters are:')
    [print(f'{f} ',end='') for f in guessed_letters]
    print('')
    if guess not in secret_word:
        print('This letter was not on the word.')
        return (guessed_letters, lives - 1)
    else:
        print("\nCorrect")
        [print('_ ', end='') if f not in guessed_letters else print(f,end='') for f in secret_word]
        print('')
        if all(f in secret_word for f in guessed_letters):
            return 'Win'
        return (guessed_letters, lives)

def get_word(difficulty:int):
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

def initialize_game():
    word = get_word(int(input('Enter a number from 0-5 to choose a difficulty\n- 0 for easy, 5 for difficult\nEnter here: ')))
    guessed_letters = []
    # guess = 'a'
    lives = 3

    while lives>0:
        guess_now = input('Enter your guess: ')
        result = update_game_state(word, guessed_letters, guess_now, lives)
        if result=='Win':
            print(f"You won!")
            print(f"The word was {word}")
            break
        guessed_letters, lives = result[0], result[1]
        if lives == 0:
            print('You lost, better luck next time')

        
initialize_game()




# update_game_state(word,guessed_letters, guess, lives)