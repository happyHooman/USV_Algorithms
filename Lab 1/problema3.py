from helpers import pretty_print

n = int(input('n='))

a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(0 if i == j else j + 1)
    a.append(b)

pretty_print(a)
