with open('input_file_1') as f:
    vect = [[int(y) for y in x.split()] for x in f.read().splitlines()]

gt = int(vect[0][0])
gv = vect[1:]
vt = 0
selected = []

print(gt)

gv.sort(key=lambda x: x[1] / x[0], reverse=True)
print(gv)

for x in gv:
    if gt > x[0]:
        selected.append(x)
        gt -= x[0]
        vt += x[1]
    elif gt > 0:
        vt += (gt / x[0]) * x[1]
        gt = 0

print(selected)
print(vt)
