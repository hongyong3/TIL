import sys
sys.stdin = open("이진탐색_input.txt")

def binarySearch(start, end, middle):
    count = 0
    while start <= end:
        count += 1
        mid = int((start + end)/2)
        if mid == middle:    # 검색 성공
            return count
        elif middle < mid:
            end = mid
        else:
            start = mid
    return None    # 검색 실패


T = int(input())
for test_case in range(1, T + 1):
    P, A, B = list(map(int, input().split()))
    result = ''
    if (binarySearch(1, P, A)) < (binarySearch(1, P, B)):
        result = 'A'
    elif (binarySearch(1, P, A)) == (binarySearch(1, P, B)):
        result = '0'
    else:
        result = 'B'

    print("#{} {}".format(test_case, result))