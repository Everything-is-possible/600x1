# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
	 score = 0
    for char in word:
        score += SCRABBLE_LETTER_VALUES[char]
    if len(word) == n:
        return score * len(word) + 50
    else:
        return score * len(word)
   


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
	'''
	>>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
	>>> displayHand(hand) # Implemented for you
	a q l l m u i
	>>> hand = updateHand(hand, 'quail') # You implement this function!
	>>> hand
	{'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
	>>> displayHand(hand)
	l m  
	'''
    # TO DO ... <-- Remove this comment when you code this function
	copyhand = hand.copy()
    for letter in word:
        #assert  letter in hand , 'wrong word'
        if letter in hand:
            copyhand[letter] -= 1
            #hand[letter] -= 1
            #if copyhand[letter] == 0:
                #del(copyhand[letter])
       
            
    return copyhand


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
	copyhand = hand.copy()
    checkhand = True
    for letter in word:
        #assert letter in hand , 'wrong word'
        if letter in hand:
            copyhand[letter] -= 1
            if copyhand[letter] == -1:
                del(copyhand[letter])
        if letter not in copyhand:
            checkhand = False
    checklist = False
    if word in wordList:
        checklist = True
    
    if (checkhand and checklist):
        return True
    else:
        return False


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
	return sum(list(hand.values())) #sum all values


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    score = 0
    summ = 0
    common = 'Enter:'
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) != 0: ## use def
        # Display the hand
        print('Current Hand:',end='')
        print(displayHand(hand)) ## use def #functon have two lines,is need use end = '' to solve the unexcepte line
        # Ask user for input
        word = input(common)
        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            break

            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False: ## use def
                # Reject invalid word (print a message followed by a blank line)
                print('invalid')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(word,n) ## use def
                summ += score
                print('"',word,'"','earned', score,' points. Total: ',summ ,'points')
                
                # Update the hand 
                hand = updateHand(hand, word)  ## use def

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if word == '.':
        print ('Goodbye! Total score: ',summ,' points.')
    else:
        print ('Run out of letters. Total score: ',summ,' points. ')

#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
	'''
	Enter n to deal a new hand, r to replay the last hand, or e to end game: r
	You have not played a hand yet. Please play a new hand first!

	Enter n to deal a new hand, r to replay the last hand, or e to end game: n
	<call to playHand> 

	Enter n to deal a new hand, r to replay the last hand, or e to end game: n
	<call to playHand> 

	Enter n to deal a new hand, r to replay the last hand, or e to end game: n
	<call to playHand> 

	Enter n to deal a new hand, r to replay the last hand, or e to end game: x
	Invalid command.
	Enter n to deal a new hand, r to replay the last hand, or e to end game: e <-----exit

	'''
	'''
	Enter n to deal a new hand, r to replay the last hand, or e to end game: r <--- complain
	You have not played a hand yet. Please play a new hand first!

	Enter n to deal a new hand, r to replay the last hand, or e to end game: n
	Current Hand: p z u t t t o
	Enter word, or a "." to indicate that you are finished: tot
	"tot" earned 9 points. Total: 9 points

	Current Hand: p z u t
	Enter word, or a "." to indicate that you are finished: .
	Goodbye! Total score: 9 points.

	Enter n to deal a new hand, r to replay the last hand, or e to end game: r  <-----back hand
	Current Hand: p z u t t t o
	Enter word, or a "." to indicate that you are finished: top
	"top" earned 15 points. Total: 15 points

	Current Hand: z u t t
	Enter word, or a "." to indicate that you are finished: tu
	Invalid word, please try again.

	Current Hand: z u t t
	Enter word, or a "." to indicate that you are finished: .
	Goodbye! Total score: 15 points.
	
	Enter n to deal a new hand, r to replay the last hand, or e to end game: e <-----exit
	'''
    # TO DO ... <-- Remove this comment when you code this function
    point = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
    #hand = ''  <---wrong
    n = HAND_SIZE
    if hand == None: # start at hand = None
        hand = {}
    if point == 'r':
        if hand == {}: # check if is at start
            print('You have not played a hand yet. Please play a new hand first!')
        else:
            playHand(hand,wordList,n) #use the unchanged(/before) hand
            
            
        
    elif point == 'n' :
        
        hand = dealHand(n)
        playHand(hand,wordList,n)
    
    elif point == 'e':
        return # exit !
    
       
        
    else:
        print('invalid')
    playGame(wordList,hand) #add another ag, so 'hand' can cahnge every loop.## keep going ,until return



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
