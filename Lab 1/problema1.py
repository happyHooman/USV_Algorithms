with open('input_data_1') as f:
    vect = f.read().splitlines()[0].split(' ')
for i in range(len(vect)):
    vect[i] = int(vect[i])

# a - suma numerelor pare
# b - cate numere sunt mai mici decat ultimul
# c - 2 cele mai mari
# d - suma numerelor din 2 cifre
# e - cate numere au ultimele 2 cifre egale

a = sum([x for x in vect if x % 2 == 0])
b = len([x for x in vect if x < vect[-1]])
c = [max(vect)] + [max([x for x in vect if x < max(vect)])]
d = sum([x for x in vect if 9 < x < 100])
e = len([x for x in vect if x > 10 and str(x)[-1] == str(x)[-2]])

print(vect)
print(a)
print(b)
print(c)
print(d)
print(e)
