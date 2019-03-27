import sys
sys.stdin = open("[PY-TST]최소 비용으로 포장 다시 하기_input.txt", "r")

def pack(data):
    global sum
    data.sort()
    data.insert(0, data.pop(0) + data.pop(0))
    sum += data[0]

for test_case in range(2):
    N = int(input())
    data = list(map(int, input().split()))
    sum = 0
    while len(data) >= 2:
        pack(data)
    print(sum)

# for test_case in range(2):
#     N = int(input())
#     data = list(map(int, input().split()))
#     sol = 0
#
#     # 단순정렬 이용하기
#     for k in range(N-1):
#     # K위치에서 2개씩만 정렬
#         for i in range(k, k+2):
#             for j in range(i+1, N):
#                 if data[i] > data[j]:
#                     data[i], data[j] = data[j], data[i]
#         data[k+1] += data[k] # K, K+1 번째 포장
#         sol += data[k+1]
#     print(sol)
#
#     # 삽입정렬 이용하기
#     data.sort()
#     for k in range(1, N):
#         data[k] += data[k-1]    # K, K+1 번째 포장
#         sol += data[k]
#         temp = data[k]
#         for i in range(k+1, N):
#             if data[i] < temp: # 크거나 같을때까지 교환
#                 data[i], data[i-1] = data[i-1], data[i]
#             else:
#                 break
#     print(sol)
