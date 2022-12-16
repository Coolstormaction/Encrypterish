assigned = {
    '1': '!',
    '2': '@',
    '3': '#', 
    '4': '$',
    '5': '%',
    '6': '^',
    '7': '&',
    '8': '*',
    '9': '(',
    '0': ')',
    '~': '`',
    '<': ',',
    '>': '.',
    '?': '/',
    '-': '_',
    '[': '{',
    ']': '}',
    '\\': '|'
}

notThird  = {
    'x': 'c', # c : x
    'y': 'b', # b : y
    'z': 'a' # a : z
}

canNotDecreaseDict = {value: key for key, value in notThird.items()}
reversedAssigned = {value: key for key, value in assigned.items()}

mainStr = "[green1]~[/]\n[bright_cyan]$[/] [green1]encrypt[/] [bright_cyan]||[/] [green1]decrypt[/] [bright_cyan]--run[/]\n[green1].\n..\n...[/]\n[bright_cyan]->[/] [green1]Do you want to encrypt [E] or decrypt [D] ?[/] [bright_cyan]<-[/]\n "
validEncryptList = ['E', 'e']
validDecryptList = ['D', 'd']
notToTheThird = ['x', 'y', 'z', 'X', 'Y', 'Z']
canNotDecrease = ['a', 'b', 'c', 'A', 'B', 'C']

def originalString(word): 
    with open("reserved.txt", "w") as f: f.write(word)