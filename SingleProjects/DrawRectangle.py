cols = -1
rows = -1

while cols < 0 or cols > 205 :
    try:
        cols = int( input( "Input width (max 205): " ) ) 
    except ValueError: 
        print ("Not a number.")
        continue
    if cols > 205: 
        print( "Too much. Try one more time." )

while rows < 0 or rows > 57 :
    try:
        rows = int( input( "Input height (max 57): " ) )
    except ValueError: 
        print ("Not a number.")
        continue
    if rows > 57: 
        print( "Too much. Try one more time." )


print("*"*cols + "\n",
("*" + " " * ( cols - 2 ) +  "*" + "\n" ) * ( rows - 2 ),
"*"*cols, sep="")