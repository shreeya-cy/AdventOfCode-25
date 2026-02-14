with open('input.txt') as f:
    inp = f.read()

lines = inp.split('\n')
mat = list()
for line in lines:
    line = [int(x) for x in line.split(',')]
    mat.append(line)

lar_area = 0
for i in range(len(mat)):
    for j in range(i+1, len(mat)):
        if lar_area <= ((abs(mat[i][0]-mat[j][0])+1) * (abs(mat[i][1]-mat[j][1])+1)):
            lar_area = (abs(mat[i][0] - mat[j][0]) + 1) * (abs(mat[i][1] - mat[j][1]) + 1)

print(lar_area)