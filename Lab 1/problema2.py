from helpers import pretty_print

n = int(input('n='))
m = int(input('m='))

a = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(min([i + 1, j + 1]))
    a.append(b)

pretty_print(a)
