with open('input.txt') as f:
    dig = f.read()
digs = dig.split('\n')
count=0
mat = []
for d in digs:
    d = list(d)
    mat.append(d)
row = len(mat)
cols = len(mat[0])

for i in range(row):
    for j in range(cols):
        if mat[i][j] == 'S':
            mat[i+1][j]='|'
        if i!=0 and mat[i-1][j]=='|' and mat[i][j] == '.':
            mat[i][j] = '|'
        if mat[i-1][j]=='|' and mat[i][j] == '^':
            mat[i][j-1] = '|'
            mat[i][j+1] = '|'

for i in range(1, row):
    for j in range(cols):
        if mat[i][j] == '^' and mat[i-1][j] == '|':
            count += 1

print(count)