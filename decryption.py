from rich.console import Console
from string import ascii_lowercase, ascii_uppercase
from errors import *
import time, getpass, strings

user = getpass.getuser()
console = Console()

class Decryption: 
    def __init__(self, word):
        self.word = word
        self.newWordList = []
        
    def decrypt(self): 
        for l in self.word: 
            if l not in strings.canNotDecrease and l not in strings.assigned.values() and l not in strings.reversedAssigned.values(): 
                self.newWordList.append(ascii_lowercase[ascii_lowercase.index(l) - 3]) if not l.isupper() else self.newWordList.append(ascii_uppercase[ascii_uppercase.index(l) - 3])
                
            if l in strings.canNotDecrease: self.newWordList.append(strings.canNotDecreaseDict[str(l)])
            if l in strings.assigned.values(): self.newWordList.append(strings.reversedAssigned[str(l)])
            if l in strings.reversedAssigned.values(): self.newWordList(strings.assigned(str(l)))
            
        with open('reserved.txt', 'r') as f:
           if self.word in f.read(): raise NotShuffledError("String not shuffled, please provide a valid string which is shuffled from ./encryption.py.")
            
        print(''.join(self.newWordList))
        self.newWordList.clear()