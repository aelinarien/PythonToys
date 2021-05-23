import curses
import time

#init curses
stdscr = curses.initscr()
curses.savetty()


max_rows = curses.LINES - 1
max_cols = curses.COLS -1

def print_table(draw_table):
    curses.curs_set(False)
    stdscr.refresh()
    for x in range(len(draw_table)):
        for y in range(len(draw_table[0])):
            stdscr.addstr(x, y, draw_table[x][y])
        

    stdscr.nodelay(1) # Don't block waiting for input.
    c = stdscr.getch() # Get char from input.  If none is available, will return -1.
    if c == 3:
        raise KeyboardInterrupt
    else:
        stdscr.nodelay(0)

    

def generate_table(rows, cols):
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

    table = [[" " for x in range(cols)] for y in range(rows)]
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

        print_table(table)
        time.sleep(0.001)



def main(stdscr):
    curses.echo()
    stdscr.keypad(True)

    #initial parameters
    cols = -1
    rows = -1
    
    while cols < 0 or cols > max_cols :
        try:
            stdscr.addstr ( "Input width (max " + str(max_cols) + "): ")
            cols = int( stdscr.getstr( ) ) 
        except ValueError: 
            stdscr.addstr ("Not a number.")
            continue
        if cols > max_cols: 
            stdscr.addstr ( "Too much. One more time." )

    while rows < 0 or rows > max_rows :
        try:
            stdscr.addstr("Input height (max " + str(max_rows) + "): ")
            rows = int( stdscr.getstr(  ) )
        except ValueError: 
            stdscr.addstr ("Not a number.")
            continue
        if rows > max_rows: 
            stdscr.addstr ( "Too much. One more time." )

    stdscr.clear()

    try:
        generate_table(rows, cols)
    except KeyboardInterrupt:
        stdscr.addstr(rows, 0, "Ctrl+C detected, Program Stopping")
        stdscr.refresh()
        time.sleep(2)
        curses.endwin()
        curses.nocbreak()

    stdscr.addstr("\nPress any key to quit.")
    stdscr.getkey()
    curses.endwin()
    curses.nocbreak()
    curses.resetty()




curses.wrapper(main)