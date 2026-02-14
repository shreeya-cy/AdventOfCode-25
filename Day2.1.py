id_ranges = input()
ids = id_ranges.split(',')
count = 0
for id in ids:
    lr, ur = id.split('-')
    lr = int(lr)
    ur = int(ur)
    for i in range(lr, ur+1):
        num = str(i)
        if(len(num)%2 == 0):
            mid = len(num)//2
            half1 = num[:mid]
            half2 = num[mid:]
            if(half1 == half2):
                count += i
print(count)

