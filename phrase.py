import game
class Phrase:
    def __init__(self,phrase):
        self.phrase = phrase.lower()
    def display(phrases, letters):
        output = []
        phrases = phrases.lower()
        phrases = list(phrases)
        for letter in phrases:
            if letter not in letters:
                output.append(letter)
            elif letter in letters:
                output.append("_")
        output = " ".join(output)
        return output
    def check_letter(phrases, guess, game_obj, letters):
        guess = guess.lower()
        try:
            if guess in letters:
                letters.remove(guess)
                if guess in phrases:
                    number = phrases.count(guess)
                    print(f"{guess} is in the phrase {number} times")
                if guess not in phrases:
                    game_obj.missed += 1
                    print(f"That was incorrect you have {game_obj.missed} incorrect guesses, if you get to five you will be eliminated")
                    pass     
            else:
                raise ValueError
        except ValueError:
            print("not a valid selection, make sure the thing you have typed is a letter that you have not guessed")
    def check_complete(phrases):
        list(phrases)
        if "_" not in phrases:
            return True
        else:
            return False
