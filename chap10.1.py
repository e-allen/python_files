# random hangman game

import random

def hangman():
    word_list = ["dog",
         "cat",
         "goat",
         "horse",
         "pig",
         "chicken",
         "goose",
         "sheep",
         "llama",
         "donkey"]
    random_number = random.randint(0, 9)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = "$"
        else:
            wrong_guesses +=1
        print((" ".join(letter_board)))
        print("\n"
              .join(stages[0: wrong_guesses + 1]))
        if "__" not in letter_board:
           print("You win! The word was:")
           print(" ".join(letter_board))
           win = True
           break
    if not win:
        print("\n"
              .join(stages[0: \
                wrong_guesses]))
        print("You lose! The word was {}."
              .format(word))
        
