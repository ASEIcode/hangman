import random

class Hangman:
    
    def __init__(self, word_list = ["apple", "kiwi", "raspberry", "grapefruit", "orange"], num_lives = 5) -> None:
        
        self.list_of_guesses = [] # list of letters already guessed 
        self.num_lives = num_lives # number of lives at start of game
        self.word_list = word_list # list of possible words for the game
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_" for letter in self.word] # list of letters guess and not guessed in word e.g. ["a", "_", "_", "l", "e"] (apple)
        self.num_letters = len(set(self.word)) # number of unique letters left to guess

    def check_guess(self, guess):
     
        guess = guess.lower()

        while self.num_lives > 0:

            if guess in list(self.word):
                print(f"\nGood guess! {guess} is in the word")
                index = 0
                for letter in self.word: # loop to update _ to letter guessed correctly
                    if letter == guess:
                        self.word_guessed[index] = letter   
                    index += 1
                self.num_letters -= 1 # reduce unique letters left to guess
                print(self.word_guessed) # print the word showing missing letters
                print(f"{self.num_letters} still left to find!") # infrom user how many letters are left to guess
                self.ask_for_input() # run the next round
                        
            else:
                print(f"\nSorry, {guess} is not in the word.")
                self.num_lives -= 1 # reduce lives
                print(f"You have {self.num_lives} lives left.")
                print(f"So far you have guessed: {self.list_of_guesses}")
                print("Please Try again.") 
                self.ask_for_input() # request another guess

    def ask_for_input(self):
        """
        Asks the user to iput a single letter. Validates this input and calls the function again if it fails
        """
        guess = input("\nGuess a letter: ")
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
            self.ask_for_input()
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
            print(f"So far you have guessed: {self.list_of_guesses}")
            self.ask_for_input()
        else:
            self.list_of_guesses.append(guess)
            self.check_guess(guess)
            

game =  Hangman()

print(f"The word for the game this time is: {game.word}")

print(game.word_guessed)

game.ask_for_input()