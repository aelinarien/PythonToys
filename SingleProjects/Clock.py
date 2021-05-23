# https://www.reddit.com/r/learnpython/comments/5uflxz/how_to_stop_the_flickering_in_this_code/
from time import sleep
from os import system, name
from datetime import datetime

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def translate(text):
    letters = []
    for letter in text:
        letters.append(LETTERS[letter])
    for line in zip(*letters):
        print (" ".join(line))


LETTERS = {
    "1": [
"  ██  ",
"████  ",
"  ██  ",
"  ██  ",
"██████"],

    "2": [
"██████",
"    ██",
"██████",
"██    ",
"██████"],

    "3": [
"██████",
"    ██",
"██████",
"    ██",
"██████"],

    "4": [
"██  ██",
"██  ██",
"██████",
"    ██",
"    ██"],

    "5": [
"██████",
"██    ",
"██████",
"    ██",
"██████"],

    "6": [
"██████",
"██    ",
"██████",
"██  ██",
"██████"],

    "7": [
"██████",
"    ██",
"    ██",
"    ██",
"    ██"],

    "8": [
"██████",
"██  ██",
"██████",
"██  ██",
"██████"],

    "9": [
"██████",
"██  ██",
"██████",
"    ██",
"██████"],

    "0": [
"██████",
"██  ██",
"██  ██",
"██  ██",
"██████"],

    ":": [
"  ",
"██",
"  ",
"██",
"  "],

    " ": [
"  ",
"  ",
"  ",
"  ",
"  "],

}

def clock():
     while 1:
        try:
            ctime = datetime.now()
            values = [ctime.hour, ctime.minute, ctime.second]
            join_values = []
            for value in values:
                svalue = str(value)
                svalue = svalue if len(svalue) == 2 else "0" + svalue
                join_values.append(svalue)
            translate(":".join(join_values))
            sleep(0.5)
            clear()
        except (KeyboardInterrupt,IOError):
            clear()
            break

clear()
clock()