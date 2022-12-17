from rich.console import Console 
from termcolor import cprint
import time, sys, os, pyfiglet
console = Console()

# String values

r_run = 'encrypt || decrypt --run'

def animate(): 
    console.print('[green1]~[/]\n[bright_cyan]$[/]')
    time.sleep(0.2)
    
    for char in r_run: sys.stdout.write(char); sys.stdout.flush(); time.sleep(0.1)
    
    time.sleep(1)
    
    print(pyfiglet.figlet_format('\nEncrypterish'))
    console.print('[green1].[/]\n'); time.sleep(2); console.print('[green1]..[/]'); time.sleep(2); console.print('[green1]...[/]'); 
    
    console.print('[bright_cyan]-> [/]', end='')
    for char in 'Do you want to encrypt [E] or decrypt [D] ?': 
        sys.stdout.write(char); sys.stdout.flush(); time.sleep(0.1)
        console.print('[bright_cyan] <-[/]\n\n', end='')
    
animate()