import random

class Hangman:
    def __init__(self, word_list, num_lives):
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
                    #print(self.word_guessed)
            self.num_letters -= 1
            print(f"There are {self.num_letters} letters left.")
        else: 
            self.num_lives -= 1
            print(f"Sorry, {guess_to_lowercase} is not in the word. Try again.")
            print(f"You have, {self.num_lives} lives left.")
    
    def ask_for_input(self):
        guess = input("Try to guess a letter: ")
        if (guess.isalpha() == False) or (len(guess) != 1):
            print("Invalid input. Please, enter a single alphabetical character.")
        elif (guess in self.list_of_guesses) == True:
            print("You already tried that letter!")
        else: 
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
                
    
def play_game(word_list):
    game = Hangman(word_list, num_lives = 5)
    while True:
        if game.num_lives == 0:
            print(f"You lost! the word was{game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break
    


fruit_list = ["apple", "banana", "pear", "grape", "melon"]
play_game(fruit_list)

        
        
        
        