# Create Letter Class
class Letter:
    letters = []
    def __init__(self,character: str,in_word: bool,not_position=[],guaruntee_position=[]) -> None:
        self.character = character.lower()
        self.in_word = in_word
        self.not_position = not_position
        self.guaruntee_position = guaruntee_position
        Letter.letters.append(self)

    def check_existing_letters(letter):
        for i in range(len(Letter.letters)):
            if Letter.letters[i].character == letter.lower():
                return Letter.letters[i]
        return None

    # Check a word against a specific letter
    def check_letter(self,word):
        # Check if the guaranteed letters are in the word
        for i in range(len(self.guaruntee_position)):
            if word[self.guaruntee_position[i]] != self.character:
                return False
        # If the letter isn't in the word
        if self.in_word == False and (self.character in word):
            return False
        # Position Stuff
        elif self.in_word and (self.character in word) and len(self.not_position) >= 1 and ((word.index(self.character)) in self.not_position):
            return False
        # If the letter is supposed to be in the word but isn't
        elif self.in_word and not (self.character in word) and len(self.not_position):
            return False
        else:
            return True

    # Check a word against all current letters
    def check(word):
        for j in range(len(Letter.letters)):
            if not Letter.letters[j].check_letter(word):
                return False
        return True