import sys
sys.stdin = open("D3_5215_input.txt", "r")

def combination(arr, r):
    arr = sorted(arr)
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            generate(chosen)
            chosen.pop()
    generate([])

combination('ABCDE', 3)





# T = int(input())
# for test_case in range(T):
#     N, L = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(N)]
