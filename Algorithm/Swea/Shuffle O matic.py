import sys
import time
start = time.time()
sys.stdin = open("test_input.txt", "r")
def dfs(depth, idx, card):
    global N, data, count
    # count가 5를 초과할 경우
    if depth > 5 or depth >= count:
        return

    # 초기상태가 이미 오름 or 내림일때, 혹은 그 상태가 됐을 때
    if card == sorted(data) or card == sorted(data, reverse=True):
        count = min(count, depth)
        return

    # card1 : 왼쪽 card2 : 오른쪽
    card1, card2 = card[:N // 2], card[N // 2:]

    # 오른쪽 shuffle 경우
    if idx >= N // 2:
        temp = card2[:(idx + 1) - (N // 2)]
        card2 = card2[(idx + 1) - (N // 2):]

    # 왼쪽 shuffle 경우
    else:
        temp = card1[:(N // 2) - (idx + 1)]
        card1 = card1[(N // 2) - (idx + 1):]

    # shuffle 합치기
    while (card1 or card2):
        if card1:
            temp.append(card1.pop(0))
        if card2:
            temp.append(card2.pop(0))

    for i in range(N - 1):
        if idx == 1 and i == 1:
            continue
        dfs(depth + 1, i, temp)

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    count = float('inf')
    for i in range(N - 1):
        dfs(0, i, data)
    if count == float('inf'):
        count = -1
    print("#{} {}".format(test_case + 1, count))
print("time :", time.time() - start)