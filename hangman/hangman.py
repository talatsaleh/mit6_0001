# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from distutils.log import warn
from multiprocessing.connection import answer_challenge
from operator import is_
import os
from pickle import FALSE
import random
import re
import string
from tokenize import String

WORDLIST_FILENAME = "F:\Work\python\hangman\words.txt"

  
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

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_letter_guessed(letter,secret_word):
  if letter in secret_word:
    return True
  else:
    return False


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
      if letter in letters_guessed:
        continue
      else:
        return FALSE
    return True



def get_guessed_word(secret_word, letters_guessed):
    guess = '\''
    for letter in secret_word:
      if letter in letters_guessed:
        guess+= letter+' '
      else:
        guess+= '_ '
    guess= guess.rstrip() + '\''

    return guess
    
       
    # FILL IN YOUR CODE HERE AND DELETE "pass"

def uniq_letters(word):
  uniqe = []
  for letter in word:
      if letter not in uniqe:
        uniqe+= letter
  return len(uniqe)

def get_available_letters(letters_guessed):
  available_letters = string.ascii_lowercase
  for letter in letters_guessed:
    if letter in available_letters:
      available_letters = available_letters.replace(letter,'')
  return available_letters
    # FILL IN YOUR CODE HERE AND DELETE "pass"
  
    
def is_letter_guessed(letter, secret_word):
  if letter in secret_word:
    return True
  else:
    False

def hangman(secret_word):
    letters_guessed = []
    vowels = 'aeiou'
    letter = None
    guesses = 6
    warning = 3
    guess = 0
    availabe_letters = None
    print('Welcome to the game Hangman!') 
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    while guesses != 0:
      print('you have',warning,'warnings left.')
      print('you have',guesses,'guesses left.')
      availabe_letters = get_available_letters(letters_guessed)
      print('available letters:',availabe_letters)
      letter = input('please guess a letter:')
      if letter == '':
        continue
      else:
        letter = letter[0]
        if letter in availabe_letters:
          letters_guessed+= letter
          if is_word_guessed(secret_word,letters_guessed) == True:
            break
          elif is_letter_guessed(letter,secret_word) == True:              
            print('good guess:',get_guessed_word(secret_word,letters_guessed))
          else:
            if letter in vowels:
              guesses-=2  
            else:  
              guesses-= 1
            print('Oops! That letter is not in my word:',get_guessed_word(secret_word,letters_guessed))
        elif letter in letters_guessed:
          warning-=1
          if warning == 0:
              guesses-= 1
              warning = 3
              print('Oops! You\'ve already guessed that letter. You now have 0 warnings:')
              print('so you have lost 1 guess:',get_guessed_word(secret_word,letters_guessed))
          else:
              print('Oops! You\'ve already guessed that letter. You now have',warning,'warnings:',get_guessed_word(secret_word,letters_guessed))
        else:
          warning-= 1
          if warning == 0:
            guesses-= 1
            warning = 3
            print('Oops, that is not valid letter. You have 0 warning left so you lost 1 guess.','you have',guesses,':', get_guessed_word(secret_word,letters_guessed))
          else:  
            print('Oops, that is not valid letter. You have',warning,'left:',get_guessed_word(secret_word,letters_guessed))
      print('------------')
    if guesses == 0:
      print('Sorry, you ran out of guesses. The word was',secret_word,'.')
    else: 
      print('------------')
      print('Congratulations, you won!')
      print('Your total score for this game is:',guesses * uniq_letters(secret_word))







# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
  my_word = my_word.replace(' ','')
  for index in range(0,len((my_word))):
    if len(my_word) != len(other_word):
      return False
    if my_word[index] == '_':
      continue
    elif my_word[index] == other_word[index]:
      continue
    else:
      return False
  return True




def show_possible_matches(my_word):
  hints = []
  for word in wordlist:
    if match_with_gaps(my_word,word):
      hints.append(word)
  if hints == []:
    print('No matches found')
    return 0
  print(*hints,sep=' ')
  



def hangman_with_hints(secret_word):
    letters_guessed = []
    letter = None
    vowels = 'aeiou'
    guesses = 6
    warning = 3
    availabe_letters = None
    print('Welcome to the game Hangman!') 
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    while guesses != 0:
      print('you have',warning,'warnings left.')
      print('you have',guesses,'guesses left.')
      availabe_letters = get_available_letters(letters_guessed)
      print('available letters:',availabe_letters)
      letter = input('please guess a letter:')
      if letter == '':
        continue
      else:
        letter = letter[0]
        if letter == '*':
          print('Possible word matches are:')
          show_possible_matches(get_guessed_word(secret_word,letters_guessed).replace('\'',''))
        elif letter in availabe_letters:
          letters_guessed+= letter
          if is_word_guessed(secret_word,letters_guessed) == True:
            break
          elif is_letter_guessed(letter,secret_word) == True:              
            print('good guess:',get_guessed_word(secret_word,letters_guessed))
          else:
            if letter in vowels:   
              guesses-= 2
            else:
              guesses-= 1
            print('Oops! That letter is not in my word:',get_guessed_word(secret_word,letters_guessed))
        elif letter in letters_guessed:
          warning-=1
          if warning == 0:
              guesses-= 1
              warning = 3
              print('Oops! You\'ve already guessed that letter. You now have 0 warnings:')
              print('so you have lost 1 guess:',get_guessed_word(secret_word,letters_guessed))
          else:
              print('Oops! You\'ve already guessed that letter. You now have',warning,'warnings:',get_guessed_word(secret_word,letters_guessed))
        else:
          warning-= 1
          if warning == 0:
            guesses-= 1
            warning = 3
            print('Oops, that is not valid letter. You have 0 warning left so you lost 1 guess.','you have',guesses,':', get_guessed_word(secret_word,letters_guessed))
          else:  
            print('Oops, that is not valid letter. You have',warning,'left:',get_guessed_word(secret_word,letters_guessed))
      print('------------')
    if guesses == 0:
      print('Sorry, you ran out of guesses. The word was',secret_word,'.')
    else: 
      print('------------')
      print('Congratulations, you won!')
      print('Your total score for this game is:',guesses * uniq_letters(secret_word))
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
        
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
