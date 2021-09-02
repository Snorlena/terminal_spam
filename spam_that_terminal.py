#This program will flood the terminal with characters. 

import random

list_of_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
"t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
 "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "\"",
  "#", "¤", "%", "&", "/", "(", ")", "=", "?", "'", "`", "^", "*", "~"]

colors = ["\x1b[1;30;40m", "\x1b[1;31;40m", "\x1b[1;32;40m", "\x1b[1;33;40m", "\x1b[1;34;40m", "\x1b[1;35;40m", 
"\x1b[1;36;40m", "\x1b[1;37;40m"]

while True:
    #This will take a random character from the list and print it in the terminal.
    print(colors[random.randint(0, 6)] + list_of_chars[random.randint(0,76)],'\x1b[0m', end="")