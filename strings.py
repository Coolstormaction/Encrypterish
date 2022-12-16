assigned = {
    1: '!',
    2: '@',
    3: '#',
    4: '$',
    5: '%',
    6: '^',
    7: '&',
    8: '*',
    9: '(',
    0: ')'
}

mainStr = "[green1]~[/]\n[bright_cyan]$[/] [green1]encrypt[/] [bright_cyan]||[/] [green1]decrypt[/] [bright_cyan]--run[/]\n[green1].\n..\n...[/]\n[bright_cyan]->[/] [green1]Do you want to encrypt [E] or decrypt [D] ?[/] [bright_cyan]<-[/]\n "
validEncryptList = ['E', 'e']
validDecryptList = ['D', 'd']

def originalString(word): 
    with open("reserved.txt", "w") as f:
        f.write(word)