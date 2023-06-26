word = "apple" #  remove when connected to random word generator

def check_guess(guess):
    """
    Takes a single letter argument (guess) from the ask_for_input() function 
    and checks if it is present in the current random word. 
    Calls the ask_for_input() function again if the letter is not present.
    Prints the message "Good guess! {guess} is in the word" if it is present.

    args: guess (string)

    returns: incorrect guess = ask_for_input() / correct guess = end
    """
    guess = guess.lower()

    incorrect_guess = True # condition to break while loop
    while incorrect_guess: # loops as long as the guess is incorrect

        if guess in list(word):
            print(f"Good guess! {guess} is in the word")
            incorrect_guess = False #breaks while loop
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            return ask_for_input() # request another guess
    return print("Test completed!") # delete this later. Only for testing

def ask_for_input():
    """
    Asks the user to iput a single letter. Validates this input and calls the function again if it fails
    """
    guess = input("Guess a letter: ")
    while not guess.isalpha() or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
            ask_for_input()
    return check_guess(guess)

ask_for_input()