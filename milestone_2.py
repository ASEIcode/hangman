import random
word_list = ["apple", "kiwi", "raspberry", "grapefruit", "orange"]

word = random.choice(word_list)

guess = input("Enter a single Letter: ")

if guess.isalpha() and len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
