import sys
sys.stdin = open("D3_2806_input.txt", "r")


def nQueen(sol, n):
    global count

    if len(sol) == n:  # 정답 배열(sol)의 길이가 n과 같아지면, count 증가
        count += 1
        return 0
    candidate = list(range(n))  # 0부터 n-1까지를 후보 배열로 만든다.
    for i in range(len(sol)):
        if sol[i] in candidate:  # 같은 열에 있는 지 확인
            candidate.remove(sol[i])  # 같은 열에 있다면 후보에서 제외
        distance = len(sol) - i
        if sol[i] + distance in candidate:  # 같은 대각성 상(+)에 있는 지 확인
            candidate.remove(sol[i] + distance)  # 같은 대각선 상에 있다면 후보에서 제외
        if sol[i] - distance in candidate:  # 같은 대각선 상(-)에 있는 지 확인
            candidate.remove(sol[i] - distance)  # 같은 대각선 상에 있다면 후보에서 제외
    if candidate != []:
        for i in candidate:
            sol.append(i)  # 후보의 요소를 정답 배열의 i+1로 추가
            nQueen(sol, n)  # 재귀적으로 다음 행도 확인
    else:
        return 0


T = int(input())
for test_case in range(T):
    N = int(input())
    count = 0
    for i in range(N):
        nQueen([i], N)
    print("#{} {}".format(test_case + 1, count))