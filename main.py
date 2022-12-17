__author__ = "Debarka Naskar"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2022 Debarka"
__version__ = "0.0.1"
__maintainer__ = "Debarka Naskar"
__email__ = "halderhena05@gmail.com"
__status__ = "Development"

from encryption import Encryption;
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