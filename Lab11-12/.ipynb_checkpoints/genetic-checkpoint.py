import numpy as np
from copy import deepcopy

from helpers import pretty_print, read_matrix_from_file


def generate_cromosoms(size):
    opts = list(range(1, 10))
    c = []
    for i in range(size):
        cr = opts[:]
        np.random.shuffle(cr)
        while cr in c:
            np.random.shuffle(cr)
        c.append(cr)
    c = np.array(c, dtype=int)
    return c


def calcul_distanta(cr):
    cr = cr.astype('int')
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
    print('-- Mutatia')
    print('Cromozomii alesi sunt:')
    pretty_print(alesi)
    for cr in alesi:
        cr = schimbare_pozitii(cr, np.random.randint(1, high=10), np.random.randint(1, high=10))
    alesi = [np.hstack((x[:-1], calcul_distanta(x[:-1]))) for x in alesi]
    print('Cromozomii mutati sunt:')
    pretty_print(alesi)
    return alesi


def recombinare(rec):
    rec = deepcopy(rec)
    np.random.shuffle(rec)
    print('-- Recombinare')
    mutanti = []
    for i in range(10):
        x = np.random.randint(2, high=8)
        m1 = rec[2*i][:x]
        m2 = rec[2*i+1][:x]
        m1c = [a for a in rec[2*i+1][x:-1] if a not in m1]
        m2c = [a for a in rec[2*i][x:-1] if a not in m2]
        m1r = [a for a in rec[2*i+1][:-1] if a not in m1 and a not in m1c]
        m2r = [a for a in rec[2*i][:-1] if a not in m2 and a not in m2c]
        m1 = np.hstack((m1, m1c, m1r))
        m2 = np.hstack((m2, m2c, m2r))
        m1 = np.hstack((m1, calcul_distanta(m1)))
        m2 = np.hstack((m2, calcul_distanta(m2)))
        mutanti.append(m1)
        mutanti.append(m2)
    mutanti = np.array(mutanti, dtype=int)
    print('Cromozomi recombinati:')
    pretty_print(mutanti)
    return mutanti


nr_cromozomi = 30
generatii = 400

distante = read_matrix_from_file('distances.in')

collection = generate_cromosoms(nr_cromozomi)
collection = [np.hstack((0, x)) for x in collection]
collection = [np.hstack((x, calcul_distanta(x))) for x in collection]
collection = sorted(collection, key=lambda x: x[10])

print('Cei 30 de cromozomi generati si sortati sunt:')
pretty_print(collection)

for u in range(generatii):
    print('Generatia', u)
    rez_mutatie = mutatie(collection[:10])
    rez_recombinare = recombinare(collection[:20])
    collection = np.vstack((collection, rez_mutatie, rez_recombinare))
    collection = np.unique(collection, axis=0)
    collection = sorted(collection, key=lambda x: x[10])
    collection = collection[:30]
    print('\n  ')

pretty_print(collection)
