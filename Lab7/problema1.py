import math
with open('input_data_1') as f:
    vector = [[int(y) for y in x.split()] for x in f.read().splitlines()][0]


def find_el(val, vect):
    mid = math.ceil((len(vect) -1) / 2)
    if len(vect) == 1:
        return 1 if vect[0] == val else -1
    if vect[mid] > val:
        return find_el(val, vect[:mid])
    elif vect[mid] < val:
        return find_el(val, vect[mid:])
    elif vect[mid] == val:
        return 1


print(find_el(99, vector))
