import sys
sys.stdin = open("도약_input.txt", "r")

N = int(input())
data = []
for i in range(N):
    data.append(int(input()))
data.sort()
# data = [list(map(int, input().split())) for _ in range(N)]

count = 0
for i in range(N-2):  # 시작위치
    for j in range(i+1, N-1): # jump1
        jump1 = data[j] - data[i]
        for k in range(j+1, N): # jump2
            jump2 = data[k] - data[j]
            if jump1 <= jump2 <= jump1 * 2:
                count += 1
            if jump2 > jump1 * 2:   # 이전 뛴거리의 2배이상이 되면 안되므로 break
                break
print(count)