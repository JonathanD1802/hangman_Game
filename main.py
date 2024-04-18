from string import punctuation, ascii_lowercase
from wordList import word_list
from random import choice
import hangman_art

letter_array = list(ascii_lowercase)
symbools_array = list(punctuation)
word_to_guess = choice(word_list)
word_to_print = ['_' for letter in word_to_guess]
player_tries = 1

print(f"{hangman_art.logo}\nThere is the character's number of the word you have to guess :")
print(word_to_guess)
while  player_tries != 6 and''.join(word_to_print) != word_to_guess:
    print(word_to_print)
    user_input = input('Please enter a letter you think the word contains : ').strip().lower()
    while not user_input in letter_array: 
        if user_input.isdigit(): 
            user_input = input('Please do not enter number.. Only letter : ')
        elif user_input in punctuation: 
            user_input = input('Please do not enter punctuation symbols :  ')
        else:
            user_input = input('Please Enter only one letter : ')
        
    if user_input in word_to_print: 
        print(f"You've already guessed the letter {user_input}")
    elif user_input in word_to_guess: 
        for i in range(len(word_to_guess)): 
            if word_to_guess[i] == user_input: 
                word_to_print[i] = user_input
    else: 
        print(f"You've guessed the letter {user_input} that is not in the word...Unfortunately, you lose a life.")
        player_tries +=1
        print(hangman_art.hangman_step[player_tries])
        

if player_tries == 6: 
    print("Sorry, you've been hanged😢... Game Over...")
else: 
    print(f"Congratulation 🥳, You've guessed the word :  {''.join(word_to_print)}")