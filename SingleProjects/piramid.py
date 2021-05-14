"""
Posłuchaj tej historii: chłopiec i jego ojciec, programista komputerowy, bawią się drewnianymi klockami. Budują piramidę.
Ich piramida jest nieco dziwna, ponieważ w rzeczywistości jest to ściana w kształcie piramidy - jest płaska. Piramida jest ułożona w stos zgodnie z jedną prostą zasadą: każda dolna warstwa zawiera jeden blok więcej niż jedna warstwa wyżej.
Twoim zadaniem jest napisanie programu, który odczytuje liczbę bloków, które mają budowniczowie i podaje wysokość piramidy (liczbę warstw), którą można osiągnąć za pomocą tych bloków.
Uwaga: wysokość mierzona jest liczbą w pełni ukończonych warstw - jeśli budowniczowie nie mają wystarczającej liczby bloków i nie mogą ukończyć kolejnej warstwy, kończą swoją pracę natychmiast.
Przetestuj swój kod za pomocą danych testowych poniżej.

Dane testowe:
Przykładowe dane wejściowe: 6
Oczekiwany wynik: Wysokość piramidy wynosi: 3
Przykładowe dane wejściowe: 20
Oczekiwany wynik: Wysokość piramidy wynosi: 5
Przykładowe dane wejściowe: 1000
Oczekiwany wynik: Wysokość piramidy wynosi: 44
Przykładowe dane wejściowe: 2
Oczekiwany wynik: Wysokość piramidy wynosi: 1
"""

blokow = int(input("Wprowadź liczbę bloków: "))


wysokosc = 0
while True:
    blokow -= ( wysokosc + 1 ) 
    if blokow < 0:
        break
    wysokosc +=1
    
    
print("Wysokość piramidy wynosi:", wysokosc)
