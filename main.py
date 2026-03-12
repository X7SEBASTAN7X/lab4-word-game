def update_game_state(secret_word, guessed_letters,guess, lives):
    if guess not in guessed_letters:
        guessed_letters += guess
    else:
        print('Already guessed this letter')
    if guess not in secret_word:
        return (guessed_letters, lives - 1)
    else:
        print("Correct")
        [print('_ ', end='') if f not in guessed_letters else print(f,end='') for f in secret_word]
        
        return (guessed_letters, lives)

word = "cebolla"
guessed_letters = []
guess = 'a'
lives = 3

update_game_state(word,guessed_letters, guess, lives)