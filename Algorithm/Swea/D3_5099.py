import sys
sys.stdin = open("D3_5099_input.txt", "r")

# 이전 풀이
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     data = list(map(int, input().split()))
#     Q = [0] * N     # 화덕
#     i = 0           # 인덱스
#
#     while i < M:               # 피자를 다 넣을 동안
#         Q[0] = [data[i], i]     # 치즈와 인덱스 넣기
#         Q.append(Q.pop(0))      # 회전
#         i += 1                  # 인덱스를 하나씩 증가시켜 모든 피자를 넣을 수 있돌고 한다.
#
#         while 0 not in Q:      # 화덕에 빈 곳이 없을 때
#             if 0 not in Q:
#                 Q[0][0] = Q[0][0] // 2  # 피자가 한 바퀴 돌면 치즈를 반으로 줄여준다.
#                 if Q[0][0] == 0:        # 치즈가 0이 되면 새로운 피자를 넣기
#                     break
#                 Q.append(Q.pop(0))      # 다시 회전시킨다.
#
#     while len(Q) >= 1:                  # 마지막 피자 구하기
#         if len(Q) == 1:                  # 답을 출력
#             print(f'#{test_case} {Q[-1][1] + 1}')
#             break
#         if Q[0][0] == 0:                # 치즈가 0인 것을 꺼낸다.
#             Q.pop(0)
#         else:
#             Q[0][0] = Q[0][0] // 2      # 피자가 한 바퀴 돌면 치즈를 반으로 줄여준다.
#             if Q[0][0] == 0:            # 치즈가 0이되면 피자를 꺼내준다.
#                 Q.pop(0)
#             else:
#                 Q.append(Q.pop(0))      # 회전시킨다.

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    pizza = [[x + 1, y] for x, y in enumerate(list(map(int, input().split())))]
    oven = [0] * N

    while pizza:
        oven[0] = pizza.pop(0)
        oven.append(oven.pop(0))

        while 0 not in oven:
            oven[0][1] //= 2
            if not oven[0][1]:
                break
            oven.append(oven.pop(0))

    while oven:
        if len(oven) == 1:
            print("#{} {}".format(test_case + 1, oven[0][0]))
            break
        if not oven[0][1]:
            oven.pop(0)
        else:
            oven[0][1] //= 2
            oven.append(oven.pop(0))