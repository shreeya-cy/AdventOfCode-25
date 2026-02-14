with open("input.txt", "r") as f:
    joltages = f.read()

joltage = joltages.split('\n')
total = 0
for j in joltage:
    # print(j)
    fnum = 0
    num = 0
    for i in range(0, len(j)):
        if fnum < int(j[i]):
            k = i+1
            while k<=len(j)-1:
                if num < ((int(j[i])*10) + int(j[k])):
                    num = (int(j[i])*10) + int(j[k])
                k+=1
    # print(num)
    total+=num

print(total)
