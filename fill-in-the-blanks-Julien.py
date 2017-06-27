# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!


def selectDifficulty():
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
    else:
        print("You've chosen " + difficulty + '!' + '\n'*2 + "You will get 5 guesses per problem\n")
        return difficulty


def answerList(p):
    if p == 'easy':
        return ['function', 'parameters', 'None', 'list']


def selectText(m):
    easyText = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
    adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
    don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
    tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
    
    if m == 'easy':
        return easyText
    
def theGame():
    #Selecting the difficulty, the answer list and text, according to difficulty
    mode = selectDifficulty()
    listAnswer = answerList(mode)
    text = selectText(mode)

    #Spliting the text into a list and initializing variables for the game
    textList = text.split(" ")
    numOfGuess = 5
    guessNum = 1
    
    print("The current paragraph reads as such:")
    print text
 
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
            for word in textList:
                if str(guessNum) in word:
                    index = textList.index(word)
                    textList[index] = guess
            guessNum += 1
            print '\nCorrect!' + '\n'*2
            print("The current paragraph reads as such:")
            print " ".join(textList)       
        else:
            numOfGuess -= 1
            if numOfGuess == 0:
                break
            else:
                print("That's isn't the correct answer! Let's try again; you have " + str(numOfGuess) + " trys left!" + "\n"*2)
                print("The current paragraph reads as such:")
                print " ".join(textList) + "\n"*2       
    print("\nGame over")    

#Running the game
theGame()
    
    