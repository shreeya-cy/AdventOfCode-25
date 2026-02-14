with open('input.txt') as f:
    array = f.read()
array = array.split('\n')
ranges = []
nums = []
for arr in array:
    if '-' in arr:
        ranges.append(arr)
sorted_ranges = sorted(
    ranges,
    key=lambda r: tuple(map(int, r.split('-')))
)

lower = []
upper = []
for ran in sorted_ranges:
    low, up = map(int, ran.split('-'))
    lower.append(low)
    upper.append(up)

res = 0
for i in range(len(lower)):
    count = 0
    if (i!=0 and lower[i]< upper[i-1] and upper[i]<upper[i-1]):
        continue
    else:
        count = count + (upper[i] - lower[i] + 1)
        if ( i != 0 and lower[i] <= upper[i-1]):
            count = count - (upper[i - 1] - lower[i] + 1)

    res += count

print(res)

# with open("input.txt") as f:
#     lines = f.read().splitlines()
#
# # parse ranges
# intervals = []
# for line in lines:
#     if "-" in line:
#         a, b = map(int, line.split("-"))
#         if a > b:
#             a, b = b, a  # optional safety
#         intervals.append((a, b))
#
# intervals.sort()
#
# # merge
# merged = []
# for start, end in intervals:
#     if not merged or start > merged[-1][1]:
#         merged.append([start, end])
#     else:
#         merged[-1][1] = max(merged[-1][1], end)
#
# # count unique IDs (inclusive ranges)
# count = sum(end - start + 1 for start, end in merged)
# print(count)

# 343329651880509
# 343517488742775