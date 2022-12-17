from encryption import Encryption
from decryption import Decryption
from rich.console import Console
from strings import mainStr
from errors import *
import functions, os, pyfiglet, readchar

console = Console()
os.system("cls" if os.name == 'nt' else 'clear')
while True:
    print(pyfiglet.figlet_format('Encrypterish'))
    console.print(mainStr)
    word = input("")
    functions.returnMain(word)