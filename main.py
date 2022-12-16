from encryption import Encryption
from decryption import Decryption
from rich.console import Console
from strings import mainStr
from errors import *
import functions, os

console = Console()
console.print(mainStr)
word = input('')
functions.returnMain(word)

rerun = input("\nDo you want to rerun the program? -> Yes [y] No [n]")
if rerun == 'y': 
    console = Console()
    console.print(mainStr)
    word = input('')
    functions.returnMain(word)
    
if rerun == 'n': quit(); os.remove('reserved.txt')
else: quit(); os.remove('reserved.txt')