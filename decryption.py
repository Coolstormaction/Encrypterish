# Imports 

from rich.console import Console
from string import ascii_lowercase, ascii_uppercase
from errors import *
import time, getpass, strings

# Setup environment
user = getpass.getuser()
console = Console()

# Base :class:`Decryption`
class Decryption: 
    """Generates decrypted string form a given encrypted string input which is encrypted from :file:`./encryption.py`"""
    
    def __init__(self, word):
        self.word = word
        self.newWordList = []
        
    def decrypt(self): 
        """
        Decrypts the input string and returns the original string.
        The process is the exact opposite of :class:`Encryption`.

        Raises:
            NotShuffledError: Raised when string is not shuffled.
        """
        for l in self.word: 
            if l not in strings.canNotDecrease and l not in strings.assigned.values() and l not in strings.reversedAssigned.values(): 
                self.newWordList.append(ascii_lowercase[ascii_lowercase.index(l) - 3]) if not l.isupper() else self.newWordList.append(ascii_uppercase[ascii_uppercase.index(l) - 3])
                
            if l in strings.canNotDecrease: self.newWordList.append(strings.canNotDecreaseDict[str(l)])
            if l in strings.assigned.values(): self.newWordList.append(strings.reversedAssigned[str(l)])
            if l in strings.reversedAssigned.values(): self.newWordList(strings.assigned(str(l)))
            
        # Checking for non shuffled words but provided to decrypt
        
        with open('reserved.txt', 'r') as f:
            # try-except clause to not break out of the loop
            
            try:
                # Custom errors \(￣︶￣*\))
                 
                if self.word in f.read(): raise NotShuffledError("String not shuffled, please provide a valid string which is shuffled from ./encryption.py. The below decrypted string is not valid.\n")
            
            # Printing the error to not break out of the loop 
            
            except NotShuffledError as notShuffled: print(notShuffled)
        
        print(''.join(self.newWordList))
        self.newWordList.clear()