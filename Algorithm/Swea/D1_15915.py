import sys
sys.stdin = open("D1_15915_input.txt", "r")

T = int(input())
for test_case in range(T):
    arr = list(map(int, input().split()))
    print(f'#{test_case + 1} {max(arr)}')