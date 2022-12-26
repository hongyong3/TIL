import sys
sys.stdin = open("D1_15918_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    arr = []
    for k, v in dic.items():
        arr.append([k, v])
    arr = sorted(arr)
    print(f'#{test_case + 1}', end=' ')
    for i in arr:
        print(f'{i[0]}:{i[1]}', end=' ')
    print()