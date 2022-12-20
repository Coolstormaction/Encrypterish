# Encrypterish

Encrypterish is encrypting (and decrypting) program which encrypts a given string input and provides an encrypted output. It also supports decrypting a given encrypted string input (it has to encrypted from Encrypterish btw).

## How does Encrypterish actually encrypt (or shuffle) a given string input?

In the codebase, we have two base classes, 
- Encryption
- Decryption

### Let's talk about :class:`Encryption` first

The Encrypt class takes a string input (original string) and then shuffles and gives the output. 

Behind the scenes, the shuffle method which actually shuffles it iterates over the word. \
While iterating it replaces each letter to the 3rd letter respective to it. 

### What about numbers?

As for numbers, the shuffle functions replaces them with their assigned symbol in keyboard. If you look at the keyboard, you will find that every number has a assigned punctuation symbol which can be accessed using the `Shift`  key. The process for shuffling punctuations is just the opposite, it replaces the symbol with it's assigned number on the keyboard.

### What about letters like `xyz` which cannot be replaced to the third letter? 

As for these letters, the shuffle method replaces them with `abc` respectively.

- Example \
x is replaced with a\
y is replaced with b \
z is replaced with c

### Let's talk about :class:`Decryption` now

This class is the exact opposite of the Encrypt class. After being shuffled from the Encrypt class, this class decrypts the string to it's original state. 

The hardwork in this class is all done by the decrypt method. \
This method iterates over the word and replaces the letter to the letter 3 places before it.

- Example \
d is replaced with a\
e is replaced with b\
...and so on

### What for numbers?

As for numbers, they are replaced with their corresponding symbol in the keyboard. \
And punctuations are replaced with their corresponding number in the keyboard

- Example\
! is replaced 1\
@ is replaced with 2 \
1 is replaced with !\
2 is replaced with @\
..so as we can clearly see, this class is the exact opposite of the Encrypt class.

# That's it!

If you notice bugs or want to share feedback, contact me through any of the below mediums\

- Discord - Ignis#3040 
- Email - halderhena05@gmail.com

Any questions and feedback are heartily welcome 😄. \
More improvements and pip package coming very soon (probably today lol).

#
