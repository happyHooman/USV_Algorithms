import copy

with open('input_data') as f:
    vector = [[int(y) for y in x.split()] for x in f.read().splitlines()][0]

print('numerele din fisier:', vector)

tablou = [0] * vector[0]
tablou[vector[2] - 1] = 2
print('raspuns la punctul 2:', tablou)
solutions = []


def check_greedy(pos, t):
    if 0 < pos < vector[0] - 1:
        return False if t[pos - 1] == 2 or t[pos + 1] == 2 else True
    if pos == 0:
        return False if t[-1] == 2 or t[pos + 1] == 2 else True
    if pos == vector[0] - 1:
        return False if t[pos - 1] == 2 or t[0] == 2 else True


def metoda_greedy():
    barbati = vector[0] - vector[1]
    for i in range(8):
        if check_greedy(i, tablou) and barbati > 0:
            tablou[i] = 2
            barbati -= 1
        if tablou[i] == 0:
            tablou[i] = 1

    print('rezultatul dupa metoda greedy:', tablou)


def metoda_backtracking(pos=0):
    if tablou.count(2) == vector[0] - vector[1]:
        solutions.append(copy.deepcopy(tablou))
        return False

    for i in range(pos, 8):
        old = tablou[i]
        if check_greedy(i, tablou) and tablou[i] != 2:
            tablou[i] = 2
            if metoda_backtracking(i):
                return True

        tablou[i] = old
    return False


if __name__ == '__main__':
    metoda_greedy()

    tablou = [0] * vector[0]
    tablou[vector[2] - 1] = 2
    metoda_backtracking()
    print('solutii', len(solutions))
    for x in solutions:
        for i in range(vector[0]):
            if x[i] == 0:
                x[i] = 1
        print(x)

    with open('your_file.txt', 'w') as f:
        for item in solutions:
            f.write("%s\n" % item)
