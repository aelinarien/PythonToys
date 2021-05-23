try:
    time = ( int( input( "Input number of seconds: " ) ) )
except ValueError:
    print ("Is not a number.")
    quit()

h = time // 3600
m = (time % 3600 ) // 60
s = time % 60
print(f"{time}s = {h} hours, {m} minutes, {s} seconds")
