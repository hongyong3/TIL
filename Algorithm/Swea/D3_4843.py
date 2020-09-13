import sys
sys.stdin = open("D3_4843_input.txt", "r")

# 이전 풀이
# def select(data):
#     for i in range(0, len(data)):
#         m_Index = i
#         if m_Index % 2:
#             for j in range(i+1, len(data)):
#                 if data[m_Index] > data[j]:
#                     m_Index = j
#             data[i], data[m_Index] = data[m_Index], data[i]
#
#         else:
#             for j in range(i+1, len(data)):
#                 if data[m_Index] < data[j]:
#                     m_Index = j
#             data[i], data[m_Index] = data[m_Index], data[i]
#     return ' '.join(str(i) for i in data[0:10])
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     data = list(map(int, input().split()))
#     print("#{} {}".format(test_case, select(data)))

T = int(input())
for test_case in range(T):
    N = int(input())
    data = sorted(list(map(int, input().split())))
    mat = []
    while len(mat) <= 8:
        mat.append(data.pop(- 1))
        mat.append(data.pop(0))
    print("#{}".format(test_case + 1), *mat)