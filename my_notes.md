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


# AUTOPLAY

use a random.choice to choose a letter, or start with all the letters and start by choosing one and poping from the List of available letters, and do that until you loose.

A smarter implementation could be to separate between guessed letters and correct letters, and then make a dictionary of the letters that usually come next to each other, therefore having a slightly better chance at winning.

We could also start by choosing two vowels, or in general the letters that are more likely to come in the word.

Also, another idea is making a list of MOST common letters and ignore the other ones