"""
./encryption.py

__author__ = 'Debarka'
The home of the base encryption class.
"""

# Imports 

from rich.console import Console
from string import ascii_lowercase, ascii_uppercase
import time, getpass, strings

# Setting up environment 

user = getpass.getuser()
console = Console()

# Base :class:`Encryption`
class Encryption:
    """Generates encrypted string from a given string input."""
    
    def __init__(self, word):
        """Constructor"""
        self.word = word
        self.newWordList = []
        
    def shuffle(self):
        """
        Shuffles the input string and returns a new encrypted string output.\n
        Taking one letter from the word, it replaces the letter to the third letter respective to the current letter.
        """
        strings.originalString(self.word)
        for l in self.word:
            if l not in strings.notToTheThird and not l.isnumeric() and not l in strings.assigned.values(): # Checking for letters that can not be replaced to the third letter
                self.newWordList.append(ascii_lowercase[ascii_lowercase.index(l) + 3]) if not l.isupper() else self.newWordList.append(ascii_uppercase[ascii_uppercase.index(l) + 3])
            
            if l in strings.notToTheThird: # Checking for x y z letters that can not be replaced to the third letter
                self.newWordList.append(strings.notThird[l])
            
            # Checking for numeric characters     
            if l.isnumeric(): self.newWordList.append(strings.assigned[l])
            
            # Checking for punctuation | whitespace characters 
            if l in strings.assigned.values(): self.newWordList.append(strings.reversedAssigned[l])
        
        # Printing a clean list to the console.    
        print(''.join(self.newWordList))