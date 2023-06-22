import random   
from words import words
from Letters import Letter

def get_current_word():
    pass

def get_letter_status():
    pass

def main():
    possible_words = []
    for i in range(len(words)):
        if Letter.check(words[i]):
            possible_words.append(words[i])

    for i in possible_words:
        print(i)
    while True:
        current_word

if __name__ == "__main__":
    main()