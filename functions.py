from encryption import Encryption
from decryption import Decryption
from rich.console import Console
from strings import *
from errors import *
import pyfiglet, time, rich

console = rich.console.Console()

def returnMain(word): 
    if word == "E" or word == 'e': 
        console.print('\n[green1]Enter the word you want to encrypt[/] [bright_cyan]-> [/]')
        eWord = input("")
        encryption = Encryption(eWord)
        print(pyfiglet.figlet_format('Encrypting...', width=500))
        time.sleep(2)
        encryption.shuffle()
        
    if word == "D" or word == 'd':
        console.print('\n[green1]Enter the word you want to decrypt[/] [bright_cyan]-> [/]')
        dWord = input("")
        decrypt = Decryption(dWord)
        print(pyfiglet.figlet_format('Decrypting...', width=500))
        time.sleep(2)
        decrypt.decrypt()