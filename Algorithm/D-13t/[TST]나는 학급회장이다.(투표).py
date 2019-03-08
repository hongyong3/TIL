import sys
sys.stdin = open("나는 학급회장이다_input.txt", "r")
N = int(input())
ans = [[0] * 5 for _ in range(4)]   # 행 : 후보자 열: 1, 2, 3 점수대로 4열: 합계
for i in range(N):
    score = list(map(int, input().split()))
    for j in range(1, 4):   # 후보자 3명
        ans[j][score[j-1]] += 1 # 후보자별 점수별 카운트

for i in range(1, 4):   # 후보자별 합계
    for j in range(1, 4):
        ans[i][4] += ans[i][j]*j
maxi = 1    # 1 번 후보를  max로 시작
flag = 0
for i  in range(2, 4):
    if ans[maxi][4] < ans[i][4]:    # 더 큰 합계를 비교
        maxi = 1
    elif ans[maxi][4] == ans[i][4]: # 동일 합계이면, 3점대부터 비교
        for j in range(3, 1, -1):   # 3점대부터 비교

print(maxi, ans[maxi][4])