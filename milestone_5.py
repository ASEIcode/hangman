import random

class Hangman:
    
    def __init__(self, word_list = ["apple", "kiwi", "raspberry", "grapefruit", "orange"], num_lives = 5) -> None:
        
        self.list_of_guesses = [] # list of letters already guessed 
        self.num_lives = num_lives # number of lives at start of game
        self.word_list = word_list # list of possible words for the game
        self.word = random.choice(self.word_list) #  random word generator using word_list
        self.word_guessed = ["_" for letter in self.word] # list of letters guess and not guessed in word e.g. ["a", "_", "_", "l", "e"] (apple)
        self.num_letters = len(set(self.word)) # number of unique letters left to guess

    def check_guess(self, guess):
        
        """
        Checks the guess argument received from the ask_for_input() method against the word attribute.
        If the letter matches, it adds the letter to the word_guessed attribute, replacing an underscore.
        Also decreases num_lives for incorrect guesses and decreases num_letters for each correct guess.
        args: guess
        return: None
        """
     
        guess = guess.lower()

        if guess in list(self.word):
            print(f"\nGood guess! {guess} is in the word")
            index = 0
            for letter in self.word: # loop to update _ to letter guessed correctly
                if letter == guess:
                    self.word_guessed[index] = letter   
                index += 1
            self.num_letters -= 1 # reduce unique letters left to guess
            print(self.word_guessed) # print the word showing missing letters
            print(f"{self.num_letters} still left to find!") # inform user how many letters are left to guess
                    
        else:
            print(f"\nSorry, {guess} is not in the word.")
            self.num_lives -= 1 # reduce lives
            print(f"You have {self.num_lives} lives left.")
            print(f"So far you have guessed: {self.list_of_guesses}")
            print("Please Try again.") 
            print(self.word_guessed)
            
    def ask_for_input(self):
        """
        Asks the user to iput a single letter. Validates this input and calls the function again if it fails.
        If the first two validations are passed then it calls the check_guess() method using guess as an argument.
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


def play_game(word_list):
    """
    Runs the game and defines a while loop to continue asking for guesses as long as the user has lives (num_lives)
    and still has letters left to guess (num_letters)

    args: word_list - Type: list >  a list of possible words for the random generator to pick from
    
    returns: None - used to run the methods in Hangman class.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    game_active = True
    print(
f"""
Wecome to Hangman!

The rules: 

Look at the blanks and guess letters to reveal to word.
For every wrong guess you will lose a life.
You start with 5 lives

The game starts now:

Your mystery word is: {game.word_guessed}
""")
    while game_active:
        if game.num_lives == 0:
            print(f"""\nYou Lost! GAME OVER!!\nThe correct word was {"".join(game.word)}""")
            game_active = False
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            game_active = False

play_game(["elephant", "tiger", "giraffe", "lion", "monkey", "zebra", "kangaroo", "penguin", "hippo", "crocodile"])

# Future changes:
# List of possible themes that user can choose from. A new word list for each theme
# Continue function - asks user if they would like to play again and starts the game fresh if so.





