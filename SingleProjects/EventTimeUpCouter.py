h = int(input("Start time (hours): "))
m = int(input("Start tiome (minutes): "))
d = int(input("Event duration (minutes): "))

h_end = ( h + ( d + m ) //60 )%24
m_end = ( m + d ) %60

print(h_end, ":", m_end, sep="")

