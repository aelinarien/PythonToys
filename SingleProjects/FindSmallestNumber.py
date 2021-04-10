wartosc = []

try:
    ile_liczb = int(input("Ile liczb chcesz podac: "))
    for i in range( ile_liczb ):
        wartosc.append( float( input( "Podaj liczbę {}: ".format( i + 1) ) ) )
except ValueError: 
    print ("Podaj liczbę.")
    quit()

najmniejsza = wartosc[0]
for x in range(len(wartosc)):
    if wartosc[x] < najmniejsza:
        najmniejsza = wartosc[x]


print(najmniejsza)