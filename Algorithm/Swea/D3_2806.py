import sys
sys.stdin = open("D3_2806_input.txt", "r")

# 방법 1 permutation 사용

# from itertools import permutations
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     count = 0
#     cols = range(N)
#     for combo in permutations(cols):
#         if N == len(set(combo[i] + i for i in cols)) == len(set(combo[i] - i for i in cols)):
#             count += 1
#     print("#{} {}".format(test_case + 1, count))

# 방법 2

def nQueen(sol):
    global count
    if len(sol) == N:
        count += 1
        return 0
    candidate = list(range(N))
    for i in range(len(sol)):
        distance = len(sol) - i
        if sol[i] in candidate: candidate.remove(sol[i])  # 같은 열에 놓이는지 체크 // 같은 열에 놓이면 후보군에서 제외
        if sol[i] + distance in candidate: candidate.remove(
            sol[i] + distance)  # 같은 대각선 상에 놓이는지 체크 // 같은 대각선 상에 놓이면 후보군에서 제외
        if sol[i] - distance in candidate: candidate.remove(
            sol[i] - distance)  # 같은 대각선 상에 놓이는지 체크 // 같은 대각선 상에 놓이면 후보군에서 제외

    if candidate != []:
        for i in candidate:
            sol.append(i)
            nQueen(sol)
            sol.pop()
    else:
        return 0

T = int(input())
for test_case in range(T):
    N = int(input())
    count = 0
    for i in range(N):
        nQueen([i])
    print("#{} {}".format(test_case + 1, count))