import sys
sys.stdin = open("D5_10507_input.txt", "r")

def solve():
    global ans, P
    s, e, cnt = 1, 1, 0

    while e < len(visited):
        if visited[e]:
            cnt += 1
            e += 1
            ans = max(ans, cnt)

        else:
            if not P:
                ans = max(ans, cnt)
                if not visited[s]:
                    P += 1
                s += 1
                cnt -= 1

            else:
                P -= 1
                cnt += 1
                e += 1
    return ans

T = int(input())
for test_case in range(T):
    N, P = map(int, input().split())
    data = list(map(int, input().split()))
    visited = [0] * (max(data) + 1)
    ans = P + 1
    for i in data:
        visited[i] = 1
    print("#{} {}".format(test_case + 1, solve()))