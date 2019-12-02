import sys
sys.stdin = open("[TST]오름차순 정렬 (단순정렬)_input.txt", "r")

# def swap(x, i, j):
#     x[i], x[j] = x[j], x[i]
#
# def selectionSort(x):
#     for size in reversed(range(len(x))):
#         max_i = 0
#         for i in range(1, 1+size):
#             if x[i] > x[max_i]:
#                 max_i = i
#         swap(x, max_i, size)
#
# N = input()
# data = list(map(int, input().split()))
# selectionSort(data)
# print(*data)

# Qsort
def quickSort(start, end, x):
    if start >= end:
        return
    else:
        pivot = end
        target = start

        for left in range(start, end):
            if x[left] < x[pivot]:
                x[target] , x[left] = x[left], x[target]
                target += 1

        x[target] , x[pivot] = x[pivot], x[target]
        quickSort(start, target-1, x)
        quickSort(target+1, end, x)


def mergesort(s, e):
    if s >= e: return         # 원소 하나 단위로 쪼갰으면 리턴
    m = (s + e)//2
    mergesort(s, m)           # 왼쪽 쪼개기
    mergesort(m+1, e)         # 오른쪽 쪼개기
    L, R, T = s, m+1, s
    while L <= m and R <= e:
        if data[L] < data[R]:   # 왼쪽 영역이 작으면 왼쪽 영역 값을 임시 버퍼로
            temp[T] = data[L]
            T += 1
            L += 1
        else:                 # 아니면 오른쪽 값을 임시 버퍼로
            temp[T] = data[R]
            T += 1
            R += 1
    while L <= m:             # L쪽이 남은경우 그대로 버퍼에 넣기
        temp[T] = data[L]
        T += 1
        L += 1
    while R <= e:             # R쪽이 남은경우 그대로 버퍼에 넣기
        temp[T] = data[R]
        T += 1
        R += 1
    for i in range(s, e+1):   # 원본에 복사하기
        data[i] = temp[i]

N = input()
data = list(map(int, input().split()))
temp = [0] * len(data)
mergesort(0, len(data)-1)
print(*data)