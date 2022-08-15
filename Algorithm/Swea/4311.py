import sys
sys.stdin = open("4311_input.txt", "r")

def calc(num, num2, oper):
    if oper == 1:
        num += num2
    elif oper == 2:
        num -= num2
    elif oper == 3:
        num *= num2
    else:
        if num2 == 0:
            return - 1
        num //= num2
    if 0 <= num < 1000:
        return num
    else:
        return - 1


def number3(cur, ncur):
    if cur == 3:
        return
    for num in numberKey:
        nextNum = ncur * 10 + num
        if visited[nextNum] <= cur + 1:
            continue
        visited[nextNum] = cur + 1
        q.append(nextNum)
        arr.append(nextNum)
        number3(cur + 1, nextNum)


T = int(input())
for test_case in range(T):
    N, O, M = map(int, input().split())
    numberKey = list(map(int, input().split()))
    operation = list(map(int, input().split()))
    W = int(input())
    arr = []
    limit = M + 1
    visited = [limit] * 1000
    q = []
    number3(0, 0)

    if visited[W] < limit:
        print(f'#{test_case + 1} {visited[W]}')
    else:
        while q:
            v = q.pop(0)
            for num in arr:
                cnt = visited[v] + len(str(num)) + 1
                if cnt + 1 > M:
                    continue
                for oper in operation:
                    nxt = calc(v, num, oper)
                    if nxt == - 1:
                        continue
                    if visited[nxt] <= cnt:
                        continue
                    visited[nxt] = cnt
                    q.append(nxt)
        if visited[W] < limit:
            print(f'#{test_case + 1} {visited[W] + 1}')
        else:
            print(f'#{test_case + 1} -1')