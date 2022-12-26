import sys
sys.stdin = open("D1_15928_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    print(f'#{test_case + 1} {arr[N // 2]}')
    