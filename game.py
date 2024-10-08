import random
import phrase
#creates a letter bank not just letting the player now what they can choose but the computer know what has been chosen by removing the ones they hav echosen later on
letter_bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#creates a game class to access to run on the major game things by calling the phrase class in the other file that is working behind the scenes
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = ["the teacher keeps quizzing us", "i love the jazz age", "i wanted to see the airplane cockpit", "dont make a mountain out of a molehill", "bread always falls on the buttered side"]
        self.active_phrase = ""
        self.guesses = ""
    #creates a function that selects a random phrase from the one in the list that was given
    def get_random_phrase(phrases):
        active_phrase = random.choice(phrases)
        active_phrase = str(active_phrase)
        return active_phrase
    #defines a function that welcomes the player and explains the rules
    def welcome():
        print("Hi there, if you've never played hang man before give me a second an i'll explain. If you know how to play you can just go right on past and enjoy playing")
        print("How to play hang man:\n Im going to start out by selecting a random phrase for you to guess, then you will try and guess letters that go in what looks like a blank phrase.")
        print("If you guess correctly then you will not loose a life and you will take another guess until all the blanks are filled in, but if you guess wrong you will loose a life and if you run out you will be eliminated.")
    #creates a funtion that as the name suggests, gets a guess from the player
    def get_guess():
        guesses = input("pick any letter from the alphabet besides a previous guess >> ")
        return guesses
    #creates a start function that pulls everything together to create the game and how it runs
    def start():
        #sets play to true which means they want to play and gets set to true or false when asked if they want to play again
        play = True
        #sets the complete to false which just says that they havent guess it right yet and will be set to true if they guess all the letters
        complete = False
        #calls game welcome to greet them
        Game.welcome()
        #creates main game loop that continues till they say no to playing again
        while play == True:
            #calls the game class so i can access the variables in it
            obj = Game()
            #gets a random phrase to use
            active_phrase = Game.get_random_phrase(obj.phrases)
            #makes sure its a string and not an element of a list
            active_phrase = str(active_phrase)
            #reastablishes our word bank so if they ask to play again it will be reset
            letter_bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            #creates the inside game loop that that just repeats until they guess wrong too many times or until they guess it right
            while obj.missed < 5 or complete == False:
                #creates our output(it would be printed straight away but it needs accessed to see if they completed it or not)
                output = phrase.Phrase.display(active_phrase, letter_bank)
                print(output)
                #checks if they completed the phrase
                complete = phrase.Phrase.check_complete(output)
                #if they got it right then tell them good job and break the inner game loop, or if they guessed too many times break the inner game loop
                if complete == True:
                    print("Congradulations you have completed the phrase!")
                    break
                if obj.missed == 5:
                    break
                #print out their available word bank
                print(f"unused letters: {", ".join(letter_bank)}")
                #grabs a guess so it can compare to the answer
                guesses = Game.get_guess()
                #calls the check letter to delete the letter and tell them if its in the phrase or not
                phrase.Phrase.check_letter(active_phrase, guesses, obj, letter_bank)
                print("-----------------------------------------")
            #creates one more inner game loop to ask if they want to keep playing and only breaks if they put in a yes or a no and rases a value error if not
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
        #this is if all the loops are broken meaning they didnt want to play again saying have a nice day and ends the running of the code
        print("Okay have a nice day")

