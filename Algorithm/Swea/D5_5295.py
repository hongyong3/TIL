import sys
sys.stdin = open("D5_5295_input.txt", "r")

# 1. 중복된 수부터 지우기 -> 어떤 중복된 수를 지울 지 알 수 없으므로 보류
# 2. 중복된 수를 지운 후 모두 포함되지 않은 수 지우기

T = int(input())
for test_case in range(T):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))
    print(arr1)
    print(arr2)
    print(arr3)
