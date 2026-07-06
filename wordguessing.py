import re
import random

def get_words():
    word_list = []
    meaning_list = []

    with open("dictionary.txt", "r") as file:
        for line in file:
            words = line.split()
            meaning = re.search(r'"(.*)"', line)
            if words:
                word_list.append(words[0])
            if meaning:
                meaning_list.append(meaning.group(1))

    return word_list, meaning_list

def pick_random_word():
    word_list, meaning_list = get_words()
    word_index = random.randint(0, len(word_list)-1)

    secret_word = word_list[word_index]
    meaning = meaning_list[word_index]

    return secret_word, meaning
    
def setup_game():
    secret_word, meaning = pick_random_word()
    word_length = len(secret_word)

    secret_characters = list(secret_word)
    guessed_characters = word_length * ["_"]
    remaining_attempts = word_length

    print(f"Clue: {meaning}.\nThis word is {word_length} characters long. You have {remaining_attempts} attempts left.\n")
    print(guessed_characters)

    return secret_word, secret_characters, guessed_characters, remaining_attempts

def gameplay(secret_word, secret_characters, guessed_characters, remaining_attempts):
    wrong_guessed_characters = []

    while remaining_attempts > 0 and secret_characters != guessed_characters:
        guess = input("Enter the character guess: ")

        if len(guess) != 1:
            print("You must input only one character at a time!\n")
            print(guessed_characters)

        elif guess in guessed_characters or guess in wrong_guessed_characters:
            print("You have already tried this character! Enter a new character.\n")
            print(guessed_characters)

        elif guess in secret_characters and guess not in guessed_characters:
            index_of_char = [i for i, val in enumerate(secret_characters) if val == guess]

            print(f"The character '{guess}' is in the word! It appears {len(index_of_char)} times!\n")
            
            for letter in range(len(index_of_char)):
                guessed_characters[index_of_char[letter]] = guess

            print(guessed_characters)

        else:
            wrong_guessed_characters.append(guess)
            print(f"The character '{guess}' is not in the word. Try again!\n")
            print(guessed_characters)
            remaining_attempts -= 1
        
        print(f"You have {remaining_attempts} attempts left.\n")

    if remaining_attempts >= 0 and secret_characters == guessed_characters:
        print(f"You have won! The word was '{secret_word}'!")
    else:
        print(f"You have lost! The word was '{secret_word}'!")

    return

def main():
    secret_word, secret_characters, guessed_characters, remaining_attempts = setup_game()
    gameplay(secret_word, secret_characters, guessed_characters, remaining_attempts)

    return

if __name__ == "__main__":
    main()