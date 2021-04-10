def check_prime( prime ):
    _prime = prime
    if _prime < 2:
        return False
    i = 2
    while i*i <= _prime:
        if (_prime % i == 0):
            return False
        i += 1
    return True

try:
    prime = ( int( input( "Give range number for prime numbers: " ) ) )
except ValueError:
    print ("Podaj liczbę.")
    quit()

i = 1;
while i < prime:
    if (check_prime(i)):
        print (i, end=" ")
    i += 1

