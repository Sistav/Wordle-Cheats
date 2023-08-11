import random   
from words import words
from Letters import Letter

def get_current_word():
    while True:
        currentword = input("Please enter the word used:\n")
        if currentword.isalpha() and len(currentword) == 5:
            return currentword
        else:
            print("That is an invalid word")

def extract_letters(word):
    for i in range(len(word)):

        existing = Letter.check_existing_letters(word[i])

        if existing == None:
            current_status = get_letter_status(word[i])
            if current_status == 1:
                Letter(word[i],True,guaruntee_position = [i])
            elif current_status == 2:
                Letter(word[i],True,[i])
            else:
                Letter(word[i],False)
        elif (existing.in_word != False):
            current_status = get_letter_status(word[i],True)
            if current_status == 1:
                existing.guaruntee_position.append(i)
            if current_status == 2:
                existing.not_position.append(i)
            
        
def get_letter_status(letter,in_word=False):
    while True:
        if in_word == False:
            letter_status = input(f"What color was the letter '{letter}'?:\n1)Green\n2)Yellow\n3)Gray\n")
            if letter_status.isnumeric() and int(letter_status) >= 1 and int(letter_status) <= 3:
                    return int(letter_status)
            else:
                print("That is an invalid input")
        else:
            letter_status = input(f"What color was the letter '{letter}'?:\n1)Green\n2)Yellow")
            if letter_status.isnumeric() and(int(letter_status) == 1 or int(letter_status) == 2) :
                    return int(letter_status)
            else:
                print("That is an invalid input")


def main():
    for i in range(5):
        word = get_current_word()
        extract_letters(word)
        possible_words = []
        for i in range(len(words)):
            if Letter.check(words[i]):
                possible_words.append(words[i])

        for i in possible_words:
            print(i)
    
    

        

if __name__ == "__main__":
    main()