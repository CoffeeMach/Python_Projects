import re
import random

def get_words():
    word_list = []
    meaning_list = []

    with open("dictionary.txt", "r") as file:
        for line in file:
            words = line.split()
            meaning = re.search(r'(?<=<).*$', line)
            if words:
                word_list.append(words[0])
            if meaning:
                meaning_list.append(meaning.group())

    return word_list, meaning_list

def pick_random_word():
    word_list, meaning_list = get_words()
    word_index = random.randint(0,49)

    secret_word = word_list[word_index]
    meaning = meaning_list[word_index]

    return secret_word, meaning
    

def main():
    return


if __name__ == "__main__":
    main()