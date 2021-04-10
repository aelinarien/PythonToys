#coding: utf8

class fitness:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def weight_kg(self):
        return self.weight / 1000

    def height_m(self):
        return self.height / 100

    def bmi (self):
        return round(self.weight_kg() / ( self.height_m() ** 2), 2)

    def rate (self):
        temp = self.bmi()
        if temp < 16.0:
            return " -- \U0001F641 wygłodzenie"
        elif temp < 16.99:
            return " -- \U0001F641 wychudzenie"
        elif temp < 18.49:
            return " -- \U0001F610 niedowaga"
        elif temp < 24.99:
            return " -- \U0001F646 Jest super!"
        elif temp < 29.99:
            return " -- \U0001F610 nadwaga"
        elif temp < 34.99:
            return " -- \U0001F62C otyłość I stopnia"
        elif temp < 39.99:
            return " -- \U0001F632 otyłość II stopnia (duza)"
        else:
            return " -- \U0001F635 otyłość III stopnia (chorobliwa)"


    def print(self):
        return ( 
        '\033[1mTwój wzrost w metrach: \033[0m' + str(self.height_m()) + 
        '\n\033[1mTwoja waga w kilogramach: \033[0m' + str(self.weight_kg()) + 
        '\n\033[1mTwoje BMI: \033[0m' + str(self.bmi())
        )

notOK = True

while(notOK):
    try:
        height = int( input ( "Podaj wzrost w cm: " ) )
        weight = int( input ( "Podaj wage w gramach: " ) )
        if( type(height) == int and type(weight) == int ):
            notOK = False
    except ValueError: 
        print ("Podaj liczbę.")
        # quit()

c = fitness( height, weight )

print ("-"*20 + "="*20 + " \U00010301\U00010311\U00010309 " + "="*20 + "-"*20 )
print ( c.print(), c.rate() )
