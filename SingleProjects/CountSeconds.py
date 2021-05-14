try:
    time = ( int( input( "Podaj ilość sekund: " ) ) )
except ValueError:
    print ("Podaj liczbę.")
    quit()

h = time // 3600
m = (time % 3600 ) // 60
s = time % 60
print(f"{time}s = {h} godzin, {m} minut, {s} sekund")
