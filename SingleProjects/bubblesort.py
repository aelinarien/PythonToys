list = [8, 10, 6, 2, 4, 5, 5, 1, 2, 3]


flag = True
while flaga:
    flag = False
    for i in range(len(list) -1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            flag = True

print(list)

