import sys
sys.stdin = open("[TST] 책꽂이_input.txt", "r")

<<<<<<< HEAD
def bookshelf(idx, sums):
    global minn
    if sums - B >= minn:
        return

    if idx == N:
        if 0 <= sums - B <= minn - 1:
            minn = sums - B
        return

    bookshelf(idx + 1, sums)
    bookshelf(idx + 1, sums + data[idx])

T = int(input())
for test_case in range(T):
    N, B = map(int, input().split())
    data = [int(input()) for _ in range(N)]
    minn = float('inf')
    bookshelf(0, 0)
    print(minn)
=======
T = int(input())
for test_case in range(T):
    N, B = map(int, input().split())
    H_i = [list(input()) for _ in range(N)]
    print(H_i)
>>>>>>> 99bd1460f81cfb751d4cdfaea01f0fae18e6c33c
