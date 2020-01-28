def pretty_print(matrix):
    max_l = 0
    for row in matrix:
        for el in row:
            max_l = max(len(str(el)), max_l)
    print()
    for row in matrix:
        print(''.join(' ' * (1 + max_l - len(str(e))) + str(e) for e in row))
    print()


def read_matrix_from_file(filename):
    with open(filename) as f:
        return [[int(y) for y in x.split()] for x in f.read().splitlines()]
