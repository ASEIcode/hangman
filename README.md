# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game using python 3, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

1. Dev environment set up. Git bot was installed and created a repo called hangman with the AI core boilerplate files for the hangman project.

2. Repo cloned to local machine

## Milestone 2

1. List of possible words  defined using 5 fruits.
2. The random.choice() method was employed to choose a random word from this list of fruits. Assigned to the variable "word"
3. The user is now asked to enter a single letter. If they enter one letter the output displays a positive message, if they enter more than one letter they receive an invalid input message

## Milestone 3

Created milestone_3.py

1. check_guess() and ask_for_input function added. 

    ### Check guess: 
    Takes a single letter argument (guess) from the ask_for_input() function 
    and checks if it is present in the current random word. 
    Calls the ask_for_input() function again if the letter is not present.
    Prints the message "Good guess! {guess} is in the word" if it is present.

    args: guess (string)

    returns: incorrect guess = ask_for_input() / correct guess = end

    ### ask_for_input()
    Asks the user to iput a single letter. Validates this input and calls the function again if it fails

2. Comments and doc strings added to keep code clear




