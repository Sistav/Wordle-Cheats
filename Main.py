import random   
from words import words

class Letter:
    letters = []
    def __init__(self,character: str,in_word: bool,position=None) -> None:
        self.character = character.lower()
        self.in_word = in_word
        self.position = position
        Letter.letters.append(self)

    def check_letter(self,word):
        if self.in_word == False and (self.character in word):
            return False
        elif self.in_word and (self.character in word) and self.position != None  and self.position != word.index(self.character) + 1:
            return False
        elif self.in_word and not (self.character in word):
            return False
        else:
            return  True

    def check(word):
        for j in range(len(Letter.letters)):
            if not Letter.letters[j].check_letter(word):
                return False
        return True

def main():
    possible_words = []
    Letter("m",True)
    Letter("n",True)
    Letter("a",False)
    Letter("i",False)
    Letter("e",False)
    Letter("o",True,2)
    Letter("w",False)
    Letter("y",False)
    Letter("u",True)
    Letter("v",False)

    for i in range(len(words)):
        if Letter.check(words[i]):
            possible_words.append(words[i])

    for i in possible_words:
        print(i)

if __name__ == "__main__":
    main()