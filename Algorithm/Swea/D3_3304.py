import sys
sys.stdin = open("D3_3304_input.txt", "r")

def lcs(a, b):
    prev = [0] * len(a)
    for i,r in enumerate(a):
        current = []
        for j, c in enumerate(b):
            if r == c:
                e = prev[j - 1] + 1 if i * j > 0 else 1
            else:
                e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)
            current.append(e)
        prev = current
    return  current[-1]

T = int(input())
for test_case in range(T):
    data1, data2 = map(str, input().split())
    print("#{} {}".format(test_case + 1, lcs(data1, data2)))