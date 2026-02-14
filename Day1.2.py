with open("input.txt", "r") as f:
    dial = f.read()
prev_num = 50
dials = dial.split()
password = 0
total = 0
count = 0
for d in dials:
    direction = d[0]
    number = int(d[1:])

    while number >= 100:
        password+=1
        number-=100

    if direction == 'L':
        total = ((prev_num - number) + 100) % 100
        if prev_num - number < 0 and prev_num!=0:
            password += 1
        prev_num = total
    else:
        total = ((prev_num + number) + 100) % 100
        if prev_num + number > 100:
            password += 1
        prev_num = total

    if (total == 0):
        password += 1


print(password)