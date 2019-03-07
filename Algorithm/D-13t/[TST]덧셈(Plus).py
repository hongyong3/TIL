import sys
sys.stdin = open("덧셈_input.txt", "r")
SASB, X = list(map(int, input().split()))
arr = str(SASB)
N = len(arr)

# 2개의 정수로 분리
for i in range(N-1):
    if int(arr[:i + 1]) + int(arr[i + 1:]) == int(X):
        print("{}+{}={}".format(int(arr[:i + 1]), int(arr[i + 1:]), int(X)))
        break
else:
    print('NONE')


# 3개의 정수로 분리
# for i in range(N-2):    # A정수 끝요소 제어
#     A = int(arr[:i+1])
#     for j in range(:i+1):   # B정수 끝요소 제어
#         B = int(arr[i+1:j+1])
#         C = int(arr[j+1:])
#         print(A, B, C)