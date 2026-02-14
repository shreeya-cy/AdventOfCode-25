with open('input.txt') as f:
    array = f.read()
array = array.split('\n')
ranges = []
nums = []
for arr in array:
    if '-' in arr:
        ranges.append(arr)
    if arr == '':
        continue
    if '-' not in arr:
        nums.append(int(arr))

lower = []
upper = []
for ran in ranges:
    low, up = map(int, ran.split('-'))
    lower.append(low)
    upper.append(up)

count = 0
for num in nums:
    for i in range(0, len(lower)):
        if num >= lower[i] and num <= upper[i]:
            count+=1
            break

print(count)