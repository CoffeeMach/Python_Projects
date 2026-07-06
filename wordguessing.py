import re

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

    dictionary = dict(zip(word_list, meaning_list))

    return dictionary
    

def main():
    get_words()


if __name__ == "__main__":
    main()