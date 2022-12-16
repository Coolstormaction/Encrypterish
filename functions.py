from encryption import Encryption
from decryption import Decryption
from rich.console import Console
from strings import *
from errors import *

def returnMain(word): 
    if word == "E" or word == 'e': 
        eWord = input("\nEnter the word you want to encrypt -> ")
        encryption = Encryption(eWord)
        encryption.shuffle()
        
    if word == "D" or word == 'd': 
        dWord = input("\nEnter the word you want to decrypt -> ")
        decrypt = Decryption(dWord)
        decrypt.decrypt()