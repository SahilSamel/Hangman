
import random
import string

WORDLIST_FILENAME = "words.json"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    
    return random.choice(wordlist)
    


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    t=0
    c=len(secret_word)
    for letter in letters_guessed:
        for char in secret_word:
            if char==letter:
                t+=1
            else:
                pass
    if c==t:
        return True
    else:
        return False

            
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters and underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    guessed_letters=[]
    for char in secret_word:
        guessed_letters.append('_ ')
    for letter in letters_guessed:
        l=0
        for char in secret_word:
            if char==letter:
                guessed_letters[l]=char
            else:
                pass
            l += 1
    ''.join(guessed_letters)
    return ''.join(guessed_letters)

    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    all_letters= string.ascii_lowercase
    all_letters=list(all_letters)
    for letter in letters_guessed:
        t=0
        for char in all_letters:
            if char==letter:
                del all_letters[t]
                break
            else:
                pass
            t+=1
    return all_letters
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    '''
    
    print('Welcome to the game of Hangman!')
    s=len(secret_word)
    letters_guessed=[]
    print('\nI am thinking of a word',s,'letters long.')
    g=6
    w=3
    while g>0:
        print('\nYou have',g,'guesses left.')
        print('\nYou have',w,'warnings left.')
        print('\nAvailable letters:',get_available_letters(letters_guessed))
        l=input('Please guess a letter:')
        if l in letters_guessed:
            w-=1
            print('Oops,You have already guessed that letter')
            continue
        if l.isalpha()==False:
            w-=1
            print('I warn u lad,alphabets only,',w,'warnings left')
            if w==0:
                print('\nYou dumb mf.')
                break
            continue
        letters_guessed.append(l)
        for char in secret_word:
            if char==letters_guessed[-1]:
                print('Good guess:',get_guessed_word(secret_word, letters_guessed))
                break
            else:
                pass
                
        g -= 1
        if is_word_guessed(secret_word, letters_guessed)==True:
            print('\nCongratulations, You are the apex champion.')
            break
        elif g==0:
            print('\nLooks like you are out of guesses.')
            print('The word was',secret_word.upper())
            break
        elif w==0:
            print('\nYou dumb mf.')
            print('The word was',secret_word)
            break
        print('---------------------')
        
    
    
if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
