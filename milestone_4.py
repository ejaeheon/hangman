import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = list(random.choice(self.word_list))
        self.word_guessed = ["_" for _ in self.word]   # list comprehension is more efficient compared using for loop
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess_to_lowercase = guess.lower()
        if (guess_to_lowercase.isalpha() == True) and (self.word.__contains__(guess_to_lowercase) == True): 
            print(f"Good guess! {guess_to_lowercase} is in the word.")
            for list_index in range(len(self.word)):
                if guess_to_lowercase == self.word[list_index]:
                    self.word_guessed[list_index] = guess_to_lowercase
                    print(self.word_guessed)
            self.num_letters -= 1
        else: 
            self.num_lives -= 1
            print(f"Sorry, {guess_to_lowercase} is not in the word. Try again.")
            print(f"You have, {self.num_lives} lives left.")
    
    def ask_for_input(self):
        while True:
            guess = input("Try to guess a letter: ")
            if guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif (guess in self.list_of_guesses) == True:
                print("You already tried that letter!")
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)



game = Hangman(["apple", "banana", "pear", "grape", "melon"])
game.ask_for_input()
        
        
        
        