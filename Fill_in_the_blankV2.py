# IPND Stage 2 Final Project

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#Importing random library
import random


easy1 = '''1.A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

easy2 = '''2.Conditional execution in a program is essential.
The ___1___ statement check a condition and change the behavior of the program accordingly.
If the condition is not met, the ___2___ keyword can be used instead.
As for iteration, it is used to repeat execution of a set of statements. To go through a list or a string,
we can use the ___3___ loop. Finally, a ___4___ loop can be used to execute some part of the code,
an unknown number of times, as long as the condition statement remains True.'''

medium1 = '''1. In python there are four numeric types: ___1___, float, long and complex.
As for sequence data types, you can use ___2___ , ___3___ or tuples.
Finnaly, it is possible to use a ___4___ , as an associative array object composed of a collection
of (key, value) pairs.'''
#medium2

hard1 = '''1. Python is considered an ___1___ language.
The code is run by an ___2___ instead of being converted to machine code by a ___3___ .
Python supports multiple programs paradigms including ___4___ programming and object-oriented programming.'''
#hard2


def updateText(textList, guessNum, guess):
    """For a good guess this function goes
    to the appropriate text to replace blanks
    with the correct answer.
    arguments: textList: The list of the words contained in the text words are strings
               guessNum: The number of the guess to find the appropriate blank to replace with guess as an int
               guess: The guess of the user as a string
    returns: the list of the text that has been updated
    """

    for word in textList:
        if str(guessNum) in word:
            index = textList.index(word)
            textList[index] = guess
    return textList

def selectDifficulty():
    """Select the difficulty of the text to complete for the game,
       by querying the user response
       Possible choices include easy, medium, and hard
    arguments: NA
    returns: the difficulty level as a string
    """

    welcomeMessage = "Please select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard."
    print welcomeMessage
    difficultyChoices = ['easy','medium','hard']

    #Selecting difficulty from user
    difficulty = raw_input()

    #Verifying if user as selected a valid choice
    while difficulty not in difficultyChoices:
        print("That's not an option!")
        print welcomeMessage
        difficulty = raw_input()
    return difficulty


def selectGuess():
    """Select the number of guesses allowed to complete the blanks,
       by querying the user response
    arguments: NA
    returns: the number of guess as an int
    """

    while True:
        guess = raw_input('How many guesses you should have for this round?: ')

        #defense for bad entry
        try:
            if int(guess) > 0:
                break
        #Letter
        except ValueError:
            print("That's not an option!")
        #Negative number
        else:
            print("That's not an option!")
    return int(guess)


def answerList(p, num):
    """Depending of the difficulty level chosen and the number
       as input num, return the correct table for the answers
       of the text with blanks to fill
    arguments: p: the difficulty level as a string
               num: the number of the text in the category of the
                    difficulty level chosen
    returns: the corresponding answer table for the text to fill
    """

    if p == 'easy':
        #The different answers list of the easy texts
        easy1Ans = ['function', 'parameters', 'None', 'list']
        easy2Ans = ['if', 'else', 'for', 'while']
        easyAnsTab = [easy1Ans, easy2Ans]
        return easyAnsTab[num-1]

    elif p == 'medium':
       #The different answers list of the easy texts
       medium1Ans = ['int', 'lists', 'strings', 'dictionary']
       #medium2Ans = []
       #mediumAnsTab = [medium1Ans, medium2Ans]
       return medium1Ans

    elif p == 'hard':
        #The different answers list of the easy texts
        hard1Ans = ['interpreted', 'interpreter', 'compiler', 'functionnal']
        #hard2Ans = []
        #hardAnsTab = [hard1Ans, hard2Ans]
        return hard1Ans


def selectText(m, num):
    """Depending of the difficulty level chosen and the number
       as input num, return the text with blanks to fill
    arguments: p: the difficulty level as a string
               num: the number of the text in the category of the
               difficulty level chosen
    returns: the corresponding text to fill
    """

    easyTextTab =[easy1, easy2]
    mediumTextTab = [medium1]
    hardTextTab = [hard1]
    if m == 'easy':
        return easyTextTab[num-1]
    elif m == 'medium':
      return mediumTextTab[0]
    elif m == 'hard':
        return hardTextTab[0]

def theGame():
    """Main of the program where the player is ask to enter
       an answer. If the number of guesses left is 0 the game
       is over. If the player fill all the blank inside the
       number of guesses allowed, he wins
    arguments: NA
    returns: NA
    """

    #Selecting the difficulty, the answer list and text,
    #according to difficulty and the random number generated
    mode, num = selectDifficulty(), random.randint(1,2)
    listAnswer, text  = answerList(mode, num), selectText(mode, num)

    #Spliting the text into a list and initializing variables for the game
    textList = text.split(" ")
    numOfGuess, guessNum = selectGuess(), 1

    print("\nYou've chosen " + mode + '!' + '\n'*2 + "You will get " + str(numOfGuess) + " guesses per problem\n" + "The current paragraph reads as such:\n" + text)

    #main bulk of the game where the player interacts and the text gets change accordingly with good answers
    while numOfGuess > 0:
        if guessNum > len(listAnswer):
            print('\nYou have won!')
            break

        #Asking user input
        guess = raw_input('What should be substituted in for ' + '__' + str(guessNum) + '__' + '? ')

        #Checking if the guess match in the answer list at the good index with GuessNum
        #Search for the token using guessNum variable in the textList
        #Get the token index in the list and swap the token by the answer
        if guess == listAnswer[guessNum -1]:
            textList = updateText(textList, guessNum, guess)
            guessNum += 1
            print('\nCorrect!' + '\n'*2 + "The current paragraph reads as such:" + '\n' + " ".join(textList) )
        else:
            numOfGuess -= 1
            if numOfGuess == 0:
                break
            else:
                print("That's isn't the correct answer! Let's try again; you have " + str(numOfGuess) + " trys left!" + "\n"*2 + "The current paragraph reads as such:" + '\n' + " ".join(textList) + "\n"*2)
    print("\nGame over")

#Running the game
theGame()
