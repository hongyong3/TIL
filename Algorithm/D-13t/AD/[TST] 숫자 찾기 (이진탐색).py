import sys
sys.stdin = open("[TST] 숫자 찾기 (이진탐색)_input.txt", "r")

def binary_search(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = (start + end) // 2

        if key == a[middle]:    # 검색성공
            return middle + 1
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return 0

N = int(input())
data = list(map(int, input().split()))
T = int(input())
key = list(map(int, input().split()))

for i in key:
    print(binary_search(data, i))