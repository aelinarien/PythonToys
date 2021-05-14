def mysplit(string):
    list = []
    temp = ""
    # split on space
    for ch in string:
        temp += ch
        if ch == " ":
            list.append(temp[:-1])
            temp = ""
    list.append(temp)
    # remove empty strings from list
    list[:] = [x for x in list if x]
    return list


print(mysplit("Być albo nie być, oto jest pytanie"))
print(mysplit("Być albo nie być,oto jest pytanie"))
print(mysplit("    "))
print(mysplit("  abc  "))
print(mysplit(""))