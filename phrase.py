import game
#defines a class phrase to access whenever i need something to do with the phrase
class Phrase:
    def __init__(self,phrase):
        self.phrase = phrase.lower()
    #creates a fuction that outputs what should be displayed onto the concole regarding what the phrase is
    def display(phrases, letters):
        output = []
        phrases = phrases.lower()
        phrases = list(phrases)
        #this is going through every letter in the phrase to check if they have guessed it(it being gone from the word bank) and putting in a dash if it hasnt been guessed yet
        for letter in phrases:
            if letter not in letters:
                output.append(letter)
            elif letter in letters:
                output.append("_")
        #returns output of the final product of what will show up
        output = " ".join(output)
        return output
    #defines check letter so that i can access to check if the letter is in the phrase, not if the letter has been used, this also makes sure that their guess is a letter and only one letter
    def check_letter(phrases, guess, game_obj, letters):
        guess = guess.lower()
        try:
            #checks to make sure their guess is valid if not it will raise a value error
            if guess in letters:
                #removes the letter from the word bank so the display can account for it and the word bank can show an updated list
                letters.remove(guess)
                if guess in phrases:
                    #counts how many times the letter is in the phrase so it can let them know
                    number = phrases.count(guess)
                    print(f"{guess} is in the phrase {number} times")
                #updates their miss count so if they get 5 they loose
                if guess not in phrases:
                    game_obj.missed += 1
                    print(f"That was incorrect you have {game_obj.missed} incorrect guesses, if you get to five you will be eliminated")
                    pass     
            else:
                raise ValueError
        except ValueError:
            print("not a valid selection, make sure the thing you have typed is a letter that you have not guessed")
    #simply checks to see if the phrase we outputted had any dashes in it so see if they completed the phrase
    def check_complete(phrases):
        list(phrases)
        if "_" not in phrases:
            return True
        else:
            return False
