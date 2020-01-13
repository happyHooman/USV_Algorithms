import numpy as np
from copy import deepcopy

from helpers import pretty_print, get_matrix_from_file


def genereaza_cromozomi_aleatorii(size):
    # un vector cu elemente de la 1 la 9 din care se va genera cromozomul
    opts = list(range(1, 10))
    # c este lista de cromozomi, un vector de vectori
    c = []
    for i in range(size):
        # cr este un cromozom, acestui cromozom ii atribui o copie a optiunilor de la 1 la 9
        cr = opts[:]
        # functia shuffle reordoneaza in mod aleatoriu elementele cromozomului
        np.random.shuffle(cr)
        # pentru a preveni duplicatele se verifica daca cromozomul generat nu este deja in colectie
        while cr in c:
            np.random.shuffle(cr)
        # se adaoga cromozomul la colectie
        c.append(cr)
    return c


def calcul_distanta(cr):
    """calculeaza distanta descrisa de un cromozom"""
    cr = cr.astype('int')
    d = 0
    for i in range(9):
        d += distante[cr[i]][cr[i + 1]]
    d += distante[cr[-1]][0]
    return d


def schimbare_pozitii(li, p1, p2):
    """schimba cu locul 2 elemente din lista"""
    li[p1], li[p2] = li[p2], li[p1]
    return li


def mutatie(cri):
    # creez o copie separata pentru lista de cromozomi pe care ii vom muta, altfel am fi modificat lista initiala
    cri = deepcopy(cri)
    # reordonez cromozomii in mod aleatoriu, ei erau sortati dupa cea mai scurta distanta
    np.random.shuffle(cri)
    # aleg primii 5 cromozomi
    alesi = cri[:5]
    print('-- Mutatia')
    print('Cromozomii alesi sunt:')
    # functia pretty_print afiseaza in mod inteligibil o matrice bidimensionala
    pretty_print(alesi)
    for cr in alesi:
        # schimba pozitiile a 2 elemente de pe pozitii aleatorii intre 1 si 9, dorim ca "0" sa ramana primul element
        cr = schimbare_pozitii(cr, np.random.randint(1, high=10), np.random.randint(1, high=10))
    # se recalculeaza distanta cromozomului si se salveaza pe ultima pozitie din cromozom
    alesi = [np.hstack((x[:-1], calcul_distanta(x[:-1]))) for x in alesi]
    print('Cromozomii mutati sunt:')
    pretty_print(alesi)
    return alesi


def incrucisare(rec):
    # creez o copie de lucru a listei de crumozomi
    rec = deepcopy(rec)
    # reordonez cromozomii in mod aleatoriu, pentru ca asa era conditia
    np.random.shuffle(rec)
    print('-- Recombinare')
    # lista de cromozomi incrucisati
    mutanti = []
    for i in range(10):
        # pozitia de la care incepe incrucisarea,
        # am ales intre 2 si 7 pentru ca altfel nu ar fi fost posibila incrucisarea
        x = np.random.randint(2, high=8)
        # prima parte a celor 2 cromozomi, pana la punctul de incrucisare
        m1 = rec[2 * i][:x]
        m2 = rec[2 * i + 1][:x]
        # a doua parte a celor 2 cromozomi, incrucisata
        # excluzand elementele deja prezente in cromozomi
        m1c = [a for a in rec[2 * i + 1][x:-1] if a not in m1]
        m2c = [a for a in rec[2 * i][x:-1] if a not in m2]
        # elementele ramase si nelistate in fiecare cromozom in ordinea in care se gasesc in celalalt cromozom
        m1r = [a for a in rec[2 * i + 1][:-1] if a not in m1 and a not in m1c]
        m2r = [a for a in rec[2 * i][:-1] if a not in m2 and a not in m2c]
        # combinam cei 3 vectori rezultati pentru fiecare cromozom intr-unul singur
        m1 = np.hstack((m1, m1c, m1r))
        m2 = np.hstack((m2, m2c, m2r))
        # calculam distanta si o adaogam la fiecare cromozom pe ultima pozitie
        m1 = np.hstack((m1, calcul_distanta(m1)))
        m2 = np.hstack((m2, calcul_distanta(m2)))
        # adaogam cei 2 cromozomi generati in lista de cromozomi mutati
        mutanti.append(m1)
        mutanti.append(m2)
    # ma asigur ca elementele cromozomilor sunt numere intregi, si nu rationale
    mutanti = np.array(mutanti, dtype=int)
    print('Cromozomi recombinati:')
    pretty_print(mutanti)
    return mutanti


# Variablile Globale
# functia get_matrix_from file citeste un fisier si returneaza rezultatul sub forma de matrice bidimensionala
# declaratia functiei este in helpers/__init__.py, acolo pastrez functiile pe care le folosesc la mai multe laboratoare
distante = get_matrix_from_file('distances.in')

if __name__ == '__main__':
    nr_cromozomi = 30
    generatii = 400

    collection = genereaza_cromozomi_aleatorii(nr_cromozomi)
    # adaog "0" ca si punct de pornire la fiecare cromozom
    collection = [np.hstack((0, x)) for x in collection]
    # calculez distanta fiecarui cromozom si o salvez pe ultima pozitie
    collection = [np.hstack((x, calcul_distanta(x))) for x in collection]
    # sortez cromozomii dupa cea mai scurta distanta
    collection = sorted(collection, key=lambda x: x[10])

    print('Cei 30 de cromozomi generati aleatoriu si sortati sunt:')
    pretty_print(collection)

    # aici e procesul care se petrece la fiecare generatie
    for u in range(generatii):
        print('Generatia', u)
        rez_mutatie = mutatie(collection[:10])
        rez_recombinare = incrucisare(collection[:20])
        # adaugam rezultatele de mai sus la lista de cromozomi
        collection = np.vstack((collection, rez_mutatie, rez_recombinare))
        # inlaturam cromozomii duplicati
        collection = np.unique(collection, axis=0)
        # sortam cromozomii dupa cea mai scurta distanta
        collection = sorted(collection, key=lambda x: x[10])
        # pastram doar primii 30 de cromozomi, de restul nu vom avea nevoie niciodata
        # doar primii 20 de cromozomi sunt folositi la mutatie si incrucisare
        collection = collection[:30]

        # afisam primii 5 cromozomi din lista ca sa putem observa imbunatatirea rezultatelor in fiecare generatie
        print('-- Primii 5 cromozomi din generatia', u)
        pretty_print(collection[:4])
        print('\n  ')

    print('Cei mai buni cromozomi sunt:')
    pretty_print(collection)
