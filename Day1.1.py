with open("input.txt", "r") as f:
    dial = f.read()
prev_num = 50
dials = dial.split()
password = 0
total = 0
for d in dials:
    direction = d[0]
    number = int(d[1:])
    if direction == 'L':
        total = ((prev_num - number) + 100) % 100
        prev_num = total
    else:
        total = ((prev_num + number) + 100) % 100
        prev_num = total

    if(total == 0):
        password+=1

print(password)

