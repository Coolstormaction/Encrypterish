from encryption import Encryption
from decryption import Decryption
from rich.console import Console
from strings import mainStr
from errors import *
import functions, os

console = Console()
while True:
    console.print(mainStr)
    word = input('')
    functions.returnMain(word)