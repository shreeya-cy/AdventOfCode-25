id_ranges = input().strip()
ranges = id_ranges.split(',')

total = 0
for item in ranges:
    lr, ur = map(int, item.split('-'))
    for i in range(lr, ur + 1):
        s = str(i)
        if s in (s + s)[1:-1]:
            total += i

print(total)