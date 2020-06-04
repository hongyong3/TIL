import sys
sys.stdin = open("D5_5670_input.txt", "r")

# 57 / 87
def solve(n):
    global chk, ans
    if chk:
        chk = False
        n *= 2
        ans += 1
    else:
        temp = (G - n) / 2
        if temp > int(temp):
            temp = int(temp) + 1
        else:
            temp = int(temp)
        n += temp * 2
        ans += temp
    return n

T = int(input().replace('혻', ''))
for test_case in range(T):
    G, N = map(int, input().replace('혻', '').split())
    funxy = set()   # 방정식
    funa = set()    # 기울기
    chk = True  # 평행
    ans = 0
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().replace('혻', '').split())
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                a = 20001
            if y1 == y2:
                a = 0
        else:
            a = (y2 - y1) / (x2 - x1)
        funa.add(a)
        funxy.add((a, y1 - a * x1))
    if len(funa) == 1:
        fence = len(funa) + 1
    else:
        chk = False  # 교차
        fence = 2 * len(funxy)
    while fence < G:
        fence = solve(fence)
    print("#{} {}".format(test_case + 1, ans))

    # ans = G / 2 - len(funxy)
    # if ans > int(ans):
    #     ans = int(ans) + 1
    # elif ans == int(ans):
    #     ans = int(ans)

    # func = list(func)
    # for i in range(len(func)):
    #     for j in range(i + 1, len(func)):
    #         if func[i][0] != func[j][0]:
    #             chk = False # 교차
    #             break
    #         else:
    #             if func[i][1] != func[j][1]:
    #                 chk = False # 교차
    #                 break
    # ans = G / 2 - len(func)
    # if ans > int(ans):
    #     ans = int(ans) + 1
    # elif ans == int(ans):
    #     ans = int(ans)
    # print("#{} {}".format(test_case + 1, ans))
    # else:





    # data = [list(map(int, input().replace('혻', '').split())) for _ in range(N)]
    # ans = 0
    # chk = False # 평행유무
    # cnt = 0 # 일치하는 직선의 갯수


    # for i in range(N - 1):
    #     a1 = (data[i][3] - data[i][1]) / (data[i][2] - data[i][0])
    #     a2 = (data[i + 1][3] - data[i + 1][1]) / (data[i + 1][2] - data[i + 1][0])
    #     if a1 == a2:    # 평행
    #         if data[i][1] - a1 * data[i][0] == data[i + 1][1] - a2 * data[i + 1][0]:    # 일치
    #
    #     else:   # 교차
    #