import random

# task 1
word_list = ["Apple", "Banana", "Pear", "Grape", "Melon"]
print(word_list)

# task 2
word = random.choice(word_list)
print(word)

# task 3
guess = input("Please enter a single letter: ")
if (len(guess) == 1) and (guess.isalpha() == True): print("Good guess!")
else: print("Oops! That is not a valid input.")

print(guess)