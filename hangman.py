#TIP: use random.randint to get a random word from the list
from os import write
import random


def read_file(file_name): 
  #TODO: Step 1 - open file and read lines as words
    '''
    opens txt file and reads content
    '''
    file = open(file_name,"r")
    return file.readlines()
    
def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    this takes the random word ..replaces a random letter with an underscore and if its correct then the letter is displayed
    """
    PCword = random.randint(0 , len(words)-1)
    guessword = words[PCword]
    vanish = random.randint(0 , len(guessword)-2)
    yourWord = "Guess the word: " +guessword.replace(guessword[vanish],"_",1)
    print(yourWord)
    return guessword

def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    takes user input to compare to the random word
    """
    guess = input("Guess the missing letter: ") 
    return guess

def run_game(file_name): 
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    '''
    runs all functions
    '''
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    
    print('The word was: '+word)

if __name__ == "__main__":
    run_game('short_words.txt')

