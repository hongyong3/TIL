import sys
sys.stdin = open('마을 위성사진_input.txt', 'r')
T = int(input())
data = [list(map(int, input())) for _ in range(T)]

directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
def up(r, c):
    min = 999
    for direction in directions:
        next = tuple(map(sum, zip((r, c), direction)))
        if next[0] >= 0 and next[1] >= 0 and next[0] < T and next[1] < T:
            value = data[next[0]][next[1]]
            if value <= min:
                min = value
    if data[r][c] == min+1:
        result =False
    else:
        result = True
    data[r][c] = min+1
    return result

active = 1
before = 0
while active:
    active=False
    for r in range(1, T-1):
        for c in range(1, T-1):
            if data[r][c]:
                result = up(r,c)
                if not active and result:
                    active = result
before = max([item for items in data for item in items])
print(before)