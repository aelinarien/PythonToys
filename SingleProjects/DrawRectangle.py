cols = -1
rows = -1

while cols < 0 or cols > 205 :
    try:
        cols = int( input( "Podaj szerokosc (max 205): " ) ) 
    except ValueError: 
        print ("Podaj liczbę.")
        continue
    if cols > 205: 
        print( "Za dużo. Jeszcze raz." )

while rows < 0 or rows > 57 :
    try:
        rows = int( input( "Podaj wysokosc (max 57): " ) )
    except ValueError: 
        print ("Podaj liczbę.")
        continue
    if rows > 57: 
        print( "Za dużo. Jeszcze raz." )


print("*"*cols + "\n",
("*" + " " * ( cols - 2 ) +  "*" + "\n" ) * ( rows - 2 ),
"*"*cols, sep="")