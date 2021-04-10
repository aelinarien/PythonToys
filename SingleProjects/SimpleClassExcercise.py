class address:
    def __init__(self, street, code, city):
        self.street = street
        self.code = code
        self.city = city
    def print(self):
        return 'Adres: ' + self.street + ', Kod pocztowy: ' + self.code + ', Miasto: ' + self.city 



street = input( "Podaj ulice: " ) 
code = input( "Podaj kod: " ) 
city = input( "Podaj miastro: " ) 

c = address( street, code, city )

print ( c.print() )