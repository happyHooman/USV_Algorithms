from helpers import pretty_print

with open('input_data_1') as f:
    matricea = [[int(y) for y in x.split()] for x in f.read().splitlines()]

pretty_print(matricea)

vizitate = []
nod = 7

while True:
    print('suntem in nodul', nod)
    print('noduri vizitate:', vizitate)
    vizitate.append(nod)
    directii = matricea[nod - 1][:]
    print('directii disponibile:', directii)
    for x in vizitate:
        directii[x - 1] = 0
    print('directii nevizitate:', directii)
    if len([x for x in directii if x != 0]) == 0:
        print('nu mai sunt directii disponibile')
        print(f'Solutia{" nu" if len(vizitate) < 6 else ""} rezolva problema')
        break
    nod = directii.index(min([x for x in directii if x != 0])) + 1
    print('nodul ales:', nod)
    print('\n')
