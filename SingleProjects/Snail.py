from os import system, name
import time

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

# directions 
RIGHT = 1
DOWN = 2
LEFT = 3
UP = 4

# initial values for drawing
direcion = RIGHT
znak = "─"
col = 0
row = 0

cols = -1
rows = -1

while cols < 0 or cols > 205 :
    try:
        cols = int( input( "Input width (max 205): " ) ) 
    except ValueError: 
        print ("Give number.")
        continue
    if cols > 205: 
        print ( "Too much. Try one more time." )

while rows < 0 or rows > 57 :
    try:
        rows = int( input( "Input height (max 57): " ) )
    except ValueError: 
        print ("Give number.")
        continue
    if rows > 57: 
        print ( "Too much. Try one more time." )


table = [[" " for x in range(cols)] for y in range(rows)]

def print_table(draw_table):
    for x in range(len(draw_table)):
        for y in range(len(draw_table[0])):
            print (draw_table[x][y],end="")
        print ()

for i in range(rows*cols):
    table[col][row] = znak
    if direcion == RIGHT:
        if row < (cols - 1) and table[col][row+1] == " ":
            row += 1
        else:
            table[col][row] = "┐"
            znak = "│"
            col += 1
            direcion = DOWN
    elif direcion == DOWN:
        if col < rows-1 and table[col+1][row] == " ":
            col += 1
        else:
            table[col][row] = "┘"
            znak = "─"
            row -= 1
            direcion = LEFT
    elif direcion == LEFT:
        if row > 0 and table[col][row-1] == " ":
            row -= 1
        else:
            table[col][row] = "└"
            znak = "│"
            col -= 1
            direcion = UP
    elif direcion == UP:
        if col > 0 and table[col-1][row] == " ":
            col -= 1
        else:
            table[col][row] = "┌"
            znak = "─"
            row += 1
            direcion = RIGHT


    clear()
    print_table(table)
    time.sleep(0.0001)


