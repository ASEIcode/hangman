# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game using python 3, where the computer thinks of a word and the user tries to guess it.
 
------
## **Milestone 1**
------
1. Dev environment set up. Git bot was installed and created a repo called hangman with the AI core boilerplate files for the hangman project.

2. Repo cloned to local machine
------
## **Milestone 2**
------
1. List of possible words  defined using 5 fruits.
2. The random.choice() method was employed to choose a random word from this list of fruits. Assigned to the variable "word"
3. The user is now asked to enter a single letter. If they enter one letter the output displays a positive message, if they enter more than one letter they receive an invalid input message
------
## **Milestone 3**
------
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
----------------
## **Milestone 4**
----------------
Created milestone_4.py

1. The class "*Hangman*" was created

    It initialises with the following attributes:

    - ### *list_of_guesses*

        Type: list

        An empty list which will keep a record of letters that the user has already guessed

    - ### *num_lives*

        Type: int

        How many lives (or incorrect guesses) a user has before Game Over.
        This is one the possible arguments when creating an instance of the class. If nothing is entered the user will start with a default of 5 lives. 

    - ### *word_list*

        Type: list

        A list of words that the *word* variable can draw a random word from. This can be set by passing a list to the first argument when creating an instance. But if no list is given it defaults to a list of 5 fruits.

    - ### *word*

        Type: list

        A word chosen randomly from the *word_list* and split into a list of letters. Used as a comparison for *word_guessed*

    - ### *word_guessed*

        Type: list

        A list of letters guessed correctly and using underscores to show which letters have yet to be found by the user. Initialises with one underscore for each letter in the word.

    - ### *num_letters*

        Type: int

        Initialises as a count of the unique letters in the *word* variuable. Decreases by 1 each time a letter is guessed correctly.


2. ### "*check_guess(self, guess)*" method added

    - ensures that the guess argument is in lower case
    - The while loop was changed to take the number of lives into account. It will loop as long as the user has lives remaining.
    - Checks to see if guess is in *word* **if it is present**:
        1. Prints (f"\nGood guess! {guess} is in the word")
        2. Uses a for loop to update the *word_guessed" list, swapping "_" for the correct letter.
        3. Decreases the num_letters attribute by 1.
        4. Prints the updated *word_guessed* list to show which letters are now correct / missing.
        5. Prints "{num_letters} still left to find", to inform the user how many letters are still left to complete the word.
        6. calls the *ask_for_input()* method to start the next round of the game
    - If it **is not present**:
        1. Prints (f"\nSorry, {guess} is not in the word.")
        2. decreases num_lives by 1
        3. prints number of lives left
        4. Informs the user which letters they have already guessed using the *list_of_guesses* attrubute.
        5. Asks the user to try again and calls the *ask_for_input()* method to start the next round of the game.

3. ### *ask_for_input()* method added
    
    - The user is asked to guess a letter which is assigned to the *guess* variable
    - Checks if *guess* is a single letter. If not it asks for input again calling the *ask_for_input* method again.
    - Checks if the letter has already been guessed by comparing it to *list_of_guesses*. If the letter has already been guessed it informs the user and calls the *ask_for_input* method again.
    - If it passes these validations the else block appends the guessed letter to the *list_of_guesses* attribute and calls the *check_guess* method passing in the *guess* variable as its argument.

-----------------------
## **Milestone 5**
-----------------------

Created new file "milestone_5.py"

Added the *play_game(word_list)* function to contain the logic of what happens when we run the game. This takes the argument "*word_list*" which allows us to define the list of words that can be randomly chosen during the game.

Created a *game_active* while loop which will continuiously loop and check for the below conditional statements

1. Checks if the user has any lives left. (if game.num_lives == 0:). When True it Prints a Game over message and tells the user what the word is. Breaks the while loop. 
2. if this check is passed it then checks if the user has guessed all of the letters in the word correctly using (elif game.num_letters > 0:). If not it will call the ask_for_input method and prompt the user to guess a new letter.
3. if the previous check is 0 then there are no letters left to guess and the user has won the game. Prints a congratulatory message and breaks the while loop

I had to remove the while loop from the check_guess() method as this was creating an ininite loop. The play_game() while loop has taken its place.






