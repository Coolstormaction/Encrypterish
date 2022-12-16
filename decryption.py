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
            if l != any(['x', 'y', 'z']): 
                self.newWordList.append(ascii_lowercase[ascii_lowercase.index(l) - 3]) if not l.isupper() else self.newWordList.append(ascii_uppercase[ascii_uppercase.index(l) - 3])
                
        with open('reserved.txt', 'r') as f:
           if self.word in f.read(): raise NotShuffledError("String not shuffled, please provide a valid string which is shuffled from ./encryption.py.")
               
            
        print(''.join(self.newWordList))
        self.newWordList.clear()