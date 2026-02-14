with open("input.txt", "r") as f:
    digs = f.read()
matrix = list()
dig = digs.split('\n')
first = ['.']*(len(dig)+2)
matrix.append(first)
for line in dig:
    line = '.'+line+'.'
    line = list(line)
    matrix.append(line)
last = ['.']*(len(dig)+2)
matrix.append(last)


result = 0
row = len(dig)+1
col = len(dig)+1
while (True):
    res = 0
    for i in range(1,row):
        for j in range(1,col):
            if matrix[i][j] == '@':
                count = 0
                if matrix[i-1][j]=='@':
                    count+=1
                if matrix[i-1][j-1]=='@':
                    count+=1
                if matrix[i-1][j+1]=='@':
                    count+=1
                if matrix[i][j-1]=='@':
                    count+=1
                if matrix[i][j+1]=='@':
                    count+=1
                if matrix[i+1][j]=='@':
                    count+=1
                if matrix[i+1][j-1]=='@':
                    count+=1
                if matrix[i+1][j+1]=='@':
                    count+=1
                if count < 4:
                    matrix[i][j] = '.'
                    res+=1

    result = result + res
    if(res == 0):
        break

print(result)

