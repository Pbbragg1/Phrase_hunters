import random
import phrase
Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter_bank = Alphabet
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = ["the teacher keeps quizzing us", "i love the jazz age", "i wanted to see the airplane cockpit", "dont make a mountain out of a molehill", "bread always falls on the buttered side"]
        self.active_phrase = ""
        self.guesses = ""
    def get_random_phrase(phrases):
        active_phrase = random.choice(phrases)
        active_phrase = str(active_phrase)
        return active_phrase
    def welcome():
        print("Hi there, if you've never played hang man before give me a second an i'll explain. If you know how to play you can just go right on past and enjoy playing")
        print("How to play hang man:\n Im going to start out by selecting a random phrase for you to guess, then you will try and guess letters that go in what looks like a blank phrase.")
        print("If you guess correctly then you will not loose a life and you will take another guess until all the blanks are filled in, but if you guess wrong you will loose a life and if you run out you will be eliminated.")
        print("Please press enter after you have completed all the blanks")
    def get_guess():
        guesses = input("pick any letter from the alphabet besides a previous guess >> ")
        return guesses
    def game_over(missed, active_phrase):
        complete = False
        if missed == 5:
            print("Im sorry you have lost the game")
            print(f"The correct answer was:\n '{active_phrase}'")
        if complete == True:
            print(f"Congradulations you have guessed the phrase:\n '{active_phrase}'")
        else:
            pass
    def start():
        play = True
        complete = False
        Game.welcome()
        while play == True:
            obj = Game()
            active_phrase = Game.get_random_phrase(obj.phrases)
            active_phrase = str(active_phrase)
            letter_bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            while obj.missed < 5 or complete == False:
                output = phrase.Phrase.display(active_phrase, letter_bank)
                print(output)
                print(f"unused letters: {", ".join(letter_bank)}")
                guesses = Game.get_guess()
                phrase.Phrase.check_letter(active_phrase, guesses, obj, letter_bank)
                print("-----------------------------------------")
                complete = phrase.Phrase.check_complete(output)
                if complete == True:
                    break
                if obj.missed == 5:
                    break
            Game.game_over(obj.missed, active_phrase)
            while play != "Yes" or play != "yes" or play != "No" or play != "no":
                play = input("Would you like to play again? >> ")
                try:
                    if play == "Yes" or play == "yes":
                        play = True
                        break
                    if play == "No" or play == "no":
                        play = False
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Please input a valid answer")
            if play == False:
                break
        print("Okay have a nice day")
