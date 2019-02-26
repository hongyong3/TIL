import sys
sys.stdin = open("피자 굽기_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    data = list(map(int, input().split()))
    Q = [0] * N     # 화덕
    i = 0           # 인덱스

    while i < M:               # 피자를 다 넣을 동안
        Q[0] = [data[i], i]     # 치즈와 인덱스 넣기
        Q.append(Q.pop(0))      # 회전
        i += 1                  # 인덱스를 하나씩 증가시켜 모든 피자를 넣을 수 있돌고 한다.

        while 0 not in Q:      # 화덕에 빈 곳이 없을 때
            if 0 not in Q:
                Q[0][0] = Q[0][0] // 2  # 피자가 한 바퀴 돌면 치즈를 반으로 줄여준다.
                if Q[0][0] == 0:        # 치즈가 0이 되면 새로운 피자를 넣기
                    break
                Q.append(Q.pop(0))      # 다시 회전시킨다.

    while len(Q) >= 1:                  # 마지막 피자 구하기
        if len(Q) == 1:                  # 답을 출력
            print(f'#{test_case} {Q[-1][1] + 1}')
            break
        if Q[0][0] == 0:                # 치즈가 0인 것을 꺼낸다.
            Q.pop(0)
        else:
            Q[0][0] = Q[0][0] // 2      # 피자가 한 바퀴 돌면 치즈를 반으로 줄여준다.
            if Q[0][0] == 0:            # 치즈가 0이되면 피자를 꺼내준다.
                Q.pop(0)
            else:
                Q.append(Q.pop(0))      # 회전시킨다.