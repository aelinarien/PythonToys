list = [20, 10,2 ,212,121,2,1,2,5]

from random import shuffle
counter = 0
def is_sorted(data) -> bool:
    """Determine whether the data is sorted."""
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))

def bogosort(data) -> list:
    global counter
    """Shuffle data until sorted."""
    while not is_sorted(data):
        shuffle(data)
        counter += 1
    return data

sorted = bogosort(list)
print(f"{counter} =  {sorted}")