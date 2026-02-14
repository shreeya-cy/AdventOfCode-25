
with open('input.txt') as f:
    lines = f.read()
line = lines.split('\n')
mat = []
for l in line:
    arr = [int(x) for x in l.split(',')]
    mat.append(arr)

distance_mat = list()
for i in range(0, len(mat)-1):
    for j in range(i+1, len(mat)):
        dist = (mat[i][0] - mat[j][0])**2 + (mat[i][1] - mat[j][1])**2 + (mat[i][2] - mat[j][2])**2
        distance_mat.append((dist, i, j))

distance_mat.sort(key=lambda x: x[0])

parent = [x for x in range(len(mat))]
sizes = 1

def find(x):
    if x==parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

for dist, x, y in distance_mat:
    if find(x) == find(y): continue
    union(x,y)
    sizes += 1
    if(sizes == len(mat)):
        print(mat[x][0] * mat[y][0])
        break

