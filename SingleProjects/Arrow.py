import math


width = int(input("Input arrow size (>8): "))
if width < 8:
    print("Go back to school", width, "is smaller than 8 :(")
    quit()
halfWidth = math.floor(width/2)
temp = ""
print(" " * (halfWidth -1 ), "*", sep="")
for j in range(2, halfWidth):
    temp = " " * (halfWidth - j)
    temp += "*"
    temp += " " * (j  - 1)
    print(temp[:-1],''.join(reversed(temp)), sep="")
temp = "*" * math.floor(halfWidth / 2 ) + " " * math.ceil(halfWidth / 2 )
print(temp[:-1],''.join(reversed(temp)), sep="")
for j in range(2, halfWidth):
    temp = " " * (math.floor(halfWidth / 2) - 1)
    temp += "*"
    temp += " " * (math.ceil(halfWidth / 2))
    print(temp[:-1],''.join(reversed(temp)), sep="")
temp = " " * (math.floor(halfWidth / 2) - 1) + "*" * (math.ceil(halfWidth / 2)+1)
print(temp[:-1],''.join(reversed(temp)), sep="")
