import random

stages = [
'''
 ------
  |   |
      |
      |
      |
---------
      ''',
'''
 ------
  |   |
  O   |
      |
      |
---------
      ''',
'''
 ------
  |   |
  O   |
  |   |
      |
---------
      ''',
'''
 ------
  |   |
  O   |
 <|   |
      |
---------
      ''',
'''
 ------
  |   |
  O   |
 <|>  |
      |
---------
      ''',
'''
 ------
  |   |
  O   |
 <|>  |
 (    |
---------
      ''',
'''
 ------
  |   |
  O   |
 <|>  |
 ( )  |
---------
      '''
]

def read_dict():
    word_list = []

    with open("dictionary.txt", "r") as file:
        for line in file:
            word = line.split()
            if word:
                word_list.append(word[0])

    return word_list

def pick_random_word(word_list):
    random_index = random.randint(0, len(word_list) - 1)
    random_word = word_list[random_index]
    
    return random_word

def game_setup(random_word):
    word_length = len(random_word)

    random_word_letters = list(random_word)
    guessed_word = ["_"] * word_length

    return random_word_letters, guessed_word

def user_interface(random_word_letters, guessed_word):
    hangman_stage = 0
    wrong_guesses = []

    print(guessed_word, "\n")
    print(stages[hangman_stage], "\n")

    while guessed_word != random_word_letters and hangman_stage < 6:
        guess = input("Guess a letter: ")

        if not guess.isalpha():
            print("Try only one letter at a time!\n")

        elif guess in random_word_letters and guess not in guessed_word:
            print(f"The letter '{guess}' is in the word!")
            letter_index = [i for i, val in enumerate(random_word_letters) if val == guess]

            for letter in letter_index:
                guessed_word[letter] = guess

            print(guessed_word, "\n")

        elif guess not in wrong_guesses and guess not in guessed_word:
            hangman_stage += 1
            wrong_guesses.append(guess)
            print(f"Try again!")
            print(guessed_word, "\n")
            print(stages[hangman_stage], "\n")

        else:
            print("You have already tried that letter!")
            print(guessed_word, "\n")

    return guessed_word, hangman_stage

def game_end(random_word, random_word_letters, guessed_word, hangman_stage):
    if random_word_letters == guessed_word and hangman_stage < 6:
        print(f"You have won! The word was '{random_word}'.")
    else:
        print(f"You have lost! The word was '{random_word}'.")


def main():
    word_list = read_dict()
    random_word = pick_random_word(word_list)
    random_word_letters, guessed_word = game_setup(random_word)
    guessed_word, hangman_stage = user_interface(random_word_letters, guessed_word)
    game_end(random_word, random_word_letters, guessed_word, hangman_stage)

if __name__ == "__main__":
    main()