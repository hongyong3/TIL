import sys
sys.stdin = open("1952_input.txt", "r")

# 내 풀이

# def dfs(i, total):
#     global cost
#     if i >= 12:
#         cost = min(cost, total)
#         return
#     if use[i] == 0:
#         dfs(i + 1, total)
#     else:
#         dfs(i + 1, total + (use[i] * D1))
#         dfs(i + 1, total + M1)
#         dfs(i + 3, total + M3)
#
# T = int(input())
# for test_case in range(T):
#     D1, M1, M3, Y = map(int, input().split())
#     use = list(map(int, input().split()))
#     cost = Y
#     dfs(0, 0)
#     print("#{} {}".format(test_case + 1, cost))

# 다른사람 코드 고치지
t = int(input())
def dfs(i, count, add):
    global ans
    if count == 12:
        ans = min(ans, add)
        return
    if check[i] == 0:
        check[i] = 1
        if plan[i] == 0:
            dfs((i+1)%12, count + 1, add)
        else:
            dfs((i+1)%12, count+1, add + plan[i]*cost[0])
            dfs((i+1)%12, count+1, add+cost[1])
        check[i] = 0
    if check[i] == 0 and check[(i+1)%12] == 0 and check[(i+2)%12] == 0:
        check[i], check[(i+1)%12] , check[(i+2)%12] = 1,1,1
        dfs((i+3)%12, count + 3, add + cost[2])
        check[i], check[(i+1)%12], check[(i+2)%12] = 0,0,0


for i in range(t):
    ans = 99999999
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    # for j in range(12):
    check = [0]*12
    dfs(0, 0, 0)

    result = min(ans, cost[3])
    print('#%s %s' %(str(i+1), result))