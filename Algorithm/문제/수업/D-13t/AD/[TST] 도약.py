import sys
sys.stdin = open("[TST] 도약_input.txt", "r")


# 함수 2개로
def LowerSearch(s, e, data):
    # data 이상 중 가장 작은 값의 위치를 리턴
    sol = -1
    while s <= e:
        m = (s + e) // 2
        if arr[m] >= data:  # data 이상이면 왼쪽 영역 재탐색 (더 큰 값을 찾기 위해)
            sol = m
            e = m - 1
        else:
            s = m + 1
    return sol

def UpperSearch(s, e, data):
    # data 이하 중 가장 큰 값의 위치를 리턴
    sol = -1
    while s <= e:
        m = (s + e) // 2
        if arr[m] <= data:  # data 이하이면 오른쪽 영역 재탐색 ( 더 작은 값을 찾기 위해)
            sol = m
            s = m + 1
        else:
            e = m - 1
    return sol

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
cnt = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        start = arr[j] + (arr[j] - arr[i])
        end = arr[j] + (arr[j] - arr[i])*2
        low = LowerSearch(j+1, N-1, start)
        # 예외 경우 : 못찾았거나 2배이상 초과시 스킵
        if low == -1 or arr[low] > end: continue
        up = UpperSearch(j+1, N-1, end)
        cnt += (up - low + 1)
print(cnt)



# 함수 1개로
def upperSearch2(s, e, data):
    # data 이상에서 가장 큰 값의 위치 리턴
    sol = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] < data:  # 데이터 이하이면 오른쪽영역 재탐색
            s = m+1
            sol = m
        else:
            e = m-1
    return sol

# main
N = int(input())
arr = []
for i in range(N):
    i = int(input())
    arr.append(i)

arr.sort()
cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        start = arr[j] + (arr[j] - arr[i])
        end = arr[j] + (arr[j] - arr[i])*2

        up = upperSearch2(0, N-1, end+1)
        lo = upperSearch2(0, N-1, start)
        cnt += (up-lo)
print(cnt)