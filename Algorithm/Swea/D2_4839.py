import sys
sys.stdin = open("D2_4839_input.txt", "r")

# 이전 풀이
# def binarySearch(start, end, middle):
#     count = 0
#     while start <= end:
#         count += 1
#         mid = int((start + end)/2)
#         if mid == middle:    # 검색 성공
#             return count
#         elif middle < mid:
#             end = mid
#         else:
#             start = mid
#     return None    # 검색 실패
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     P, A, B = list(map(int, input().split()))
#     result = ''
#     if (binarySearch(1, P, A)) < (binarySearch(1, P, B)):
#         result = 'A'
#     elif (binarySearch(1, P, A)) == (binarySearch(1, P, B)):
#         result = '0'
#     else:
#         result = 'B'
#
#     print("#{} {}".format(test_case, result))

def binarySearch(start, end, n):
    count = 0
    while start <= end:
        mid = (start + end) // 2
        if mid == n:
            return count
        elif mid < n:
            start = mid
        else:
            end = mid
        count += 1

T = int(input())
for test_case in range(T):
    P, A, B = map(int, input().split())
    if binarySearch(1, P, A) > binarySearch(1, P, B):
        print("#{} {}".format(test_case + 1, "B"))
    elif binarySearch(1, P, A) < binarySearch(1, P, B):
        print("#{} {}".format(test_case + 1, "A"))
    else:
        print("#{} {}".format(test_case + 1, 0))