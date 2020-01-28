import math
from helpers import read_matrix_from_file


def sfis(msg):
    with open('iesire.out', 'a') as file:
        file.write(f'\n{msg}')


def schimbare_pozitii(li, p1, p2):
    """schimba cu locul 3 elemente din lista"""
    zero = li.index(0)
    print(p1, p2, zero)
    li[p1], li[p2], li[zero] = li[zero], li[p1], li[p2]


def p1():
    print('Problema 1')
    li = read_matrix_from_file('intrare.in')[0]
    print(li)


def p2():
    sfis('Problema 2')
    li = read_matrix_from_file('intrare.in')[0]
    sfis(li)
    for i in range(len(li)):
        sfis(li[i])
        while 5 < li[i] != i:
            sfis(f'am schimbat {li[i]} de pe pozitia {i} pe pozitia {li[i]}')
            schimbare_pozitii(li, i, li[i])
            sfis(li)


def adunare_recursiva(li, pos, s):
    if pos == len(li):
        return s
    else:
        return s + (li[pos] if li[pos] > 3 else 0) + adunare_recursiva(li, pos + 1, s)


def p3():
    li = read_matrix_from_file('intrare.in')[0]
    sfis('\n\nProblema 3')
    sfis(li)
    r = adunare_recursiva(li, 0, 0)
    sfis(r)


def divide(li):
    if len(li) > 1:
        mid = math.ceil(len(li) / 2)
        sfis(f'{li[:mid]}, {li[mid:]}')
        return divide(li[:mid]) + divide(li[mid:])
    else:
        return 1 if li[0] % 2 == 0 else 0


def p4():
    li = read_matrix_from_file('intrare.in')[0]
    sfis('\n\nProblema 4')
    sfis(li)
    r = divide(li)
    sfis(r)


if __name__ == '__main__':
    p1()
    p2()
    p3()
    p4()
