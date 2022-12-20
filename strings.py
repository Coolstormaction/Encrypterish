"""
strings.py

Contains strings and dictionary values necessary for the shuffling algorithm to replace characters | punctuation | whitespace with.
"""

# Assigned punctuation | characters assigned in keyboard.

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

# As these cannot be replace by the third letter, this is the dictionary to replace them

notThird  = {
    'x': 'c', # c : x
    'y': 'b', # b : y
    'z': 'a', # a : z
    'X': 'C', # C : X
    'Y': 'B', # B : Y
    'Z': 'A', # A : Z
}

# Reversed dictionaries

canNotDecreaseDict = {value: key for key, value in notThird.items()}
reversedAssigned = {value: key for key, value in assigned.items()}

# A rich parsed string provided to :class:`Console`

mainStr = "[green1]~[/]\n[bright_cyan]$[/] [green1]encrypt[/] [bright_cyan]||[/] [green1]decrypt[/] [bright_cyan]--run[/]\n\n[green1].\n..\n...[/]\n\n[bright_cyan]->[/] [green1]Do you want to encrypt [E] or decrypt [D] ?[/] [bright_cyan]<-[/]\n "

# Valid options in input fields

validEncryptList = ['E', 'e']
validDecryptList = ['D', 'd']

# As per the shuffling pattern, these characters cannot be replaced to the third character

notToTheThird = ['x', 'y', 'z', 'X', 'Y', 'Z']
canNotDecrease = ['a', 'b', 'c', 'A', 'B', 'C']

# Saving strings to :file:`reserved.txt`, so that user can't provide unshuffled strings.
def originalString(word): 
    with open("reserved.txt", "w") as f: f.write(word)