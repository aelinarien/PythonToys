# Kółko i krzyżyk
from random import randrange

def display_board(board):
    for x in board:
        print(("+" + "-" * 7) * 3 + "+")
        print(("|" + " " * 7) * 3 + "|")
        for y in x:
            print("|" + " " * 3 + str(y) + " " * 3, end="")
        print("|")
        print(("|" + " " * 7) * 3 + "|")
    print(("+" + "-" * 7) * 3 + "+")
            


def enter_move(board):
    while True:
        square = int(input("Input field number: "))
        if square < 1 or square > 9:
            print("No such field")
            continue
        row = (square - 1) // 3
        col = (square - 3 * row) - 1
        if type (board[row][col]) == int:
            board[row][col] = "O"
            return
        print("Field is occupied already")
            

def make_list_of_free_fields(board):
    elements = 0
    for row in range(3):
        for col in range(3):
            if type(board[row][col]) == int:
                elements += 1
    return elements


def victory_for(board, sign):
    col = [0,0,0]
    
    for x in board:
        if x.count(sign) == 3:
            print(f"{sign} have won!")
            return True
        for y in range(3):
            if x[y] == sign:
                col[y] += 1
            if col[y] == 3:
                print(f"{sign} have won!.")
                return True
    if ( board[0][2] == sign and board[2][0] == sign ) or ( board[0][0] == sign and board[2][2] == sign ):
        print(f"{sign} have won!.")
        return True
    return False

def draw_move(board):
    while True:
        square = randrange(9) + 1
        row = (square - 1) // 3
        col = (square - 3 * row) - 1
        if type (board[row][col]) == int:
            board[row][col] = "X"
            return
    


board = [[1,2,3],[4,'X',6],[7,8,9]]

while True:
    display_board(board)
    enter_move(board)
    if victory_for(board, "O"):
        break
    draw_move(board)
    if victory_for(board, "X"):
        break
    if make_list_of_free_fields(board) == 0:
        print("Tie!")
        break
    
display_board(board)
