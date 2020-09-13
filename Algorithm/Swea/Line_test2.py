import sys
sys.stdin = open("Line_test2_input.txt", "r")

def permute(arr):
    global mat
    ans = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            ans.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

data = list(map(int, input().split()))
N = int(input())
mat, answer, total, j = [], [], 0, 1
permute(data)
for i in mat[N]:
    total += i * 10 ** (len(data) - j)
    j += 1
print(total)