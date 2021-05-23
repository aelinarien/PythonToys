list = []

try:
    count = int(input("How many numbers You want to give: "))
    for i in range( count ):
        list.append( float( input( "Input number {}: ".format( i + 1) ) ) )
except ValueError: 
    print ("Not a number.")
    quit()

smallest = list[0]
for x in range(len(list)):
    if list[x] < smallest:
        smallest = list[x]


print(smallest)