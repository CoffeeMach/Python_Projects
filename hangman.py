import random

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

    chances = word_length

    return random_word_letters, guessed_word, chances

def draw_hangman(chances):
    life_length = chances

    lives = ["<3"] * life_length

    print(lives, "\n")

def user_interface(random_word_letters, guessed_word, chances):
    wrong_guesses = []

    print(guessed_word, "\n")

    while guessed_word != random_word_letters and chances > 0:
        draw_hangman(chances)
        guess = input("Guess a letter: ")

        if guess in random_word_letters and guess not in guessed_word:
            print(f"The letter '{guess}' is in the word!")
            letter_index = [i for i, val in enumerate(random_word_letters) if val == guess]

            for letter in letter_index:
                guessed_word[letter] = guess

            print(guessed_word, "\n")

        elif guess not in wrong_guesses and guess not in guessed_word:
            chances -= 1
            wrong_guesses.append(guess)
            print(f"Try again!")
            print(guessed_word, "\n")

        else:
            print("You have already tried that letter!")
            print(guessed_word, "\n")

    return guessed_word, chances

def game_end(random_word, random_word_letters, guessed_word, chances):
    if random_word_letters == guessed_word and chances >= 0:
        print(f"You have won! The word was '{random_word}'.")
        draw_hangman(chances)
    else:
        print(f"You have lost! The word was '{random_word}'.")


def main():
    word_list = read_dict()
    random_word = pick_random_word(word_list)
    random_word_letters, guessed_word, chances = game_setup(random_word)
    guessed_word, chances = user_interface(random_word_letters, guessed_word, chances)
    game_end(random_word, random_word_letters, guessed_word, chances)

if __name__ == "__main__":
    main()