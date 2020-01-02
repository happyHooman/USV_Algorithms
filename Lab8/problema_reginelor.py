import copy
from helpers import pretty_print

N = 8
tabla = [[0 for col in range(N)] for row in range(N)]
solutions = []


def check(r, c):
    global tabla
    for i in range(c):
        if tabla[r][i] == 1:
            return False
    for i in range(r):
        if tabla[i][c] == 1:
            return False
    for i in range(min([r, c]) + 1):
        if tabla[r - i][c - i] == 1:
            return False
    for i in range(min([N - r - 1, c]) + 1):
        if tabla[r + i][c - i] == 1:
            return False
    return True


def solve_queen_problem(column=0):
    if column >= N:
        solutions.append(copy.deepcopy(tabla))
        return False

    for r in range(N):
        if check(r, column):
            tabla[r][column] = 1
            if solve_queen_problem(column + 1):
                return True
        tabla[r][column] = 0

    return False


if __name__ == '__main__':
    solve_queen_problem()
    for sol in solutions:
        pretty_print(sol)
    print(f'in total sunt {len(solutions)} solutii')
