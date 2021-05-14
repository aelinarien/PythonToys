lista = [20, 10,2 ,212,121,2,1,2,5]
print(lista.index(5,0,20))

wytypowane = [2, 15, 41, 3, 7, 9]
wylosowane = [9, 13, 2, 44, 23, 31]
trafione = 0

if wylosowane in wytypowane:
    trafione += 1

print (trafione)


from random import shuffle
ile = 0
def is_sorted(data) -> bool:
    """Determine whether the data is sorted."""
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))

def bogosort(data) -> list:
    global ile
    """Shuffle data until sorted."""
    while not is_sorted(data):
        shuffle(data)
        ile += 1
    return data

posortowane = bogosort(lista)
print(f"{ile} =  {posortowane}")