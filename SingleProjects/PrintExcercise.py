
try:
    a = int( input( "Input a: " ) ) 
    b = int( input( "Input b: " ) )
except ValueError: 
    print ("This is not a number.")

# space formating
len1 = 4 if len(str(a + b)) < 3 else len(str(a + b))
len2 = 4 if len(str(b % a)) < 3 else len(str(b % a))
len3 = 4 if len(str(b ** a)) < 3 else len(str(b ** a))
len4 = 4 if len(str(b ** (1/a))) < 3 else len(str(b ** (1/a)))

print(('{:' + str(len1) + 's} ' + '{:' + str(len2) + 's} ' + '{:' + str(len3) + 's} ' + '{:' + str(len4) + 's} ' ).format("𝑎+𝑏", "𝑏%𝑎", "𝑏ª", "ª√𝑏"))
print(('{:' + str(len1) + 's} ' + '{:' + str(len2) + 's} ' + '{:' + str(len3) + 's} ' + '{:' + str(len4) + 's} ' ).format( str(a + b), str(b % a), str(b ** a), str(b ** (1/a))))
# print ( "𝑎+𝑏, 𝑏%𝑎, 𝑏ª, ª√𝑏" )
# print ( (a + b), b % a, b ** a, b ** (1/a) )