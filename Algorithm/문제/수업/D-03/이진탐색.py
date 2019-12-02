# 이진 탐색은 정렬이 돼있어야 함.

def binarySearch(a, key):
    start = 0
    end = len(a) -1
    while start <= end:
        middle = (start + end) // 2
        if key == a[middle]:    # 검색 성공
            return True
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return False    # 검색 실패

key = 23
data = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(data, key))