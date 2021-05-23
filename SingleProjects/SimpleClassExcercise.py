class address:
    def __init__(self, street, code, city):
        self.street = street
        self.code = code
        self.city = city
    def print(self):
        return 'Address: ' + self.street + ', Post code: ' + self.code + ', City: ' + self.city 



street = input( "Input street: " ) 
code = input( "Input post code: " ) 
city = input( "Input city: " ) 

c = address( street, code, city )

print ( c.print() )