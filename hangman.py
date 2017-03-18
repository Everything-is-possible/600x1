'''
hangman is a word game .
'''


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    done = False

    for char in lettersGuessed:
        if char in secretWord:
            done = True
        else:
            done = False
    return done

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    '''

    secretList = []
    for e in secretWord:
        secretList.append(e)
    '''
    secretList = list(secretWord)
    for i in range(len(secretList)):
        if secretList[i] not in lettersGuessed:
            secretList[i] = '_ '
    return ''.join(secretList)
            

			
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allletters = string.ascii_lowercase
    restletter = ''
    for e in allletters:
        if e not in lettersGuessed:
            restletter += e
    return restletter






def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('word is %d letters long.' % len(secretWord))
    
    lettersGuessed = [] #dont put into the loop
    n = 8
    while n > 0: # if use -1 , have n =0
        print('----------------------------')
        
        print('You have %d guesses left.' % n)
        
        
        print('Available letters : ', getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter:')
        guess = guess.lower()
        # lettersGuessed.append(guess) , same word also put in.
       
        
        
        
        #while not isWordGuessed.//// When have more than one IF, and need check at rhe same time, use contione
        
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
            continue  # continue to next IF
        lettersGuessed.append(guess) # add in the different word
        
        if guess in secretWord:
            n = n # rest chance dont change
            print('Good guess :', getGuessedWord(secretWord,lettersGuessed))
        else:
            n = n-1 #if erong, drop one chance
            print("Oops! That letter is not in my word :",getGuessedWord(secretWord,lettersGuessed))
            

            #elif guess not in secretWord:  /////IF/ELIF make it chear
                #print('Oops! That letter is not in my word:',getGuessedWord(secretWord,lettersGuessed) )
        if isWordGuessed(secretWord, lettersGuessed): # dont forger the (aaaa,bbbb)
            
            print('----------------------------')
            print('Congratulations, you won!')
            break # out loop
    if n == 0 :
        print('----------------------------')
        print('Sorry, you ran out of guesses. The word was else.')
    