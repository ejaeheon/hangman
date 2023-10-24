import random

# brought from milestone 2
word_list = ["Apple", "Banana", "Pear", "Grape", "Melon"]
word = random.choice(word_list)

def check_guess(guess):
    guess_to_lowercase = guess.lower()
    if (guess_to_lowercase.isalpha() == True) and (word.__contains__(guess_to_lowercase) == True): 
        print(f"Good guess! {guess_to_lowercase} is in the word: {word}")
    else: 
        print(f"Sorry, {guess_to_lowercase} is not in the word: {word}. Try again.")
    
def ask_for_input():
    while True:
        guess = input("Try to guess a letter: ")
        if guess.isalpha() == True: break
        else: print("Invalid letter. Please, enter a single alphabetical character.")
         
    check_guess(guess)
    