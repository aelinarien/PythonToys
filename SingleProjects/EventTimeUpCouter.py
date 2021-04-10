h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

h_end = ( h + ( d + m ) //60 )%24
m_end = ( m + d ) %60

print(h_end, ":", m_end, sep="")

