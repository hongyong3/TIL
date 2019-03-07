import sys
sys.stdin = open("반나누기_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K_Min, K_Max =  map(int, input().split())
    data = list(map(int, input().split()))

    div_class = []
    for T1 in range(1, max(data)):
        for T2 in range(T1, max(data)+1):
            A = []
            B = []
            C = []
            for i in data:
                if T2 <= i : A.append(i)
                elif T1 <= i < T2 : B.append(i)
                else : C.append(i)

            ans = [len(A), len(B), len(C)]

            if max(ans) <= K_Max and K_Min <= min(ans):
                answer = max(ans) - min(ans)
                div_class.append(answer)

    if div_class:
        print(min(div_class))
    else:
        print(-1)