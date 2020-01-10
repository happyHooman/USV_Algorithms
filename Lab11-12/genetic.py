import numpy as np
from copy import deepcopy

from helpers import pretty_print, get_matrix_from_file


def calcul_distanta(cr):
    d = 0
    for i in range(9):
        d += distante[cr[i]][cr[i + 1]]
    d += distante[cr[-1]][0]
    return d


def schimbare_pozitii(li, p1, p2):
    li[p1], li[p2] = li[p2], li[p1]
    return li


def mutatie(cri):
    cri = deepcopy(cri)
    np.random.shuffle(cri)
    alesi = cri[:5]
    print('Cromozomii alesi sunt:')
    pretty_print(alesi)
    for cr in alesi:
        cr = schimbare_pozitii(cr, np.random.randint(10), np.random.randint(10))
    print('Cromozomii mutati sunt:')
    pretty_print(alesi)


def generate_chromosoms(size):
    opts = list(range(1, 10))
    c = []
    for i in range(size):
        cr = opts[:]
        np.random.shuffle(cr)
        while cr in c:
            np.random.shuffle(cr)
        c.append(cr)
    return c


nr_cromozomi = 30
generatii = 400

distante = get_matrix_from_file('distances.in')

collection = generate_chromosoms(nr_cromozomi)
collection = [np.hstack((0, x)) for x in collection]
collection = [np.hstack((x, calcul_distanta(x))) for x in collection]
collection = sorted(collection, key=lambda x: x[10])

print('Cei 30 de cromozomi generati si sortati sunt:')
pretty_print(collection)


next_gen = []
print('Generatia 1')
print('--Mutatia')

mutatie(collection[:10])
