import numpy as np

from helpers import pretty_print

with open('distances.in') as f:
    matricea = [[int(y) for y in x.split()] for x in f.read().splitlines()]

opts = list(range(1, 10))

collection = []

for i in range(30):
    cr = opts[:]
    np.random.shuffle(cr)
    while cr in collection:
        np.random.shuffle(cr)
    collection.append(cr)

collection = np.hstack((np.zeros((30, 1), int), collection))
ds = []
for cr in collection:
    d = 0
    for i in range(9):
        d += matricea[cr[i]][cr[i + 1]]
    d += matricea[cr[-1]][0]
    ds.append(d)

ds = np.array(ds).reshape((30, 1))
collection = np.hstack((collection, ds))
collection = sorted(collection, key=lambda x: x[10])
pretty_print(collection)
