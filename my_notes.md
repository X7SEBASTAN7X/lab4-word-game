# My Original Thinking

What are the states of a game like Hangman?
    - Start
    - Waiting for a letter
    - Checkng Guess
    - Finished, Corretly guessed the word.
    - Finished, you lost.

What variables are required?
    - Current_word
    - Letters_used
    - Correct_Letters
    - Mistakes/wrong_letters

What are the rules and Invariants?
    - Words
    - Letters
    - Lives
    - 

What king of bugs and edge cases should we be careful about?
    - Repeated letters
    - Invalid Input (numbers, symbols)


# App States
    - Start
    - Waiting for a letter
    - Checkng Guess
    - Finished, Corretly guessed the word.
    - Finished, you lost.

* Optional states
    - Invalid Input
    - Repeated_guess
    - Paused, quit

# App Variables
    - Secret_word
    - Guessed letters
    - wrong guesses
    - Game state

Optional 
    - Masked word (showing guessed letters)
    - Last guess
    - Error message

# App Rules and Invariants


# App bugs