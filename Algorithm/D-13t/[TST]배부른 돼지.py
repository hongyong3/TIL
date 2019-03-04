T = int(input())
data = [list(map(str, input().split())) for _ in range(T)]
min, max = 10, 2
for i in range(T):
    if data[i][1] == 'Y':
        if int(data[i][0]) < min:
            min = int(data[i][0])
    if data[i][1] == 'N':
        if int(data[i][0]) > max:
            max = int(data[i][0])
if min <= max or min == 10 or max == 10:
    print('F')
else:
    print(min)