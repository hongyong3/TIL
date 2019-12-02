import sys
sys.stdin = open("컨테이너 운반_input.txt", "r")
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(), t.sort()
    sum = 0
    while len(w) > 0 and len(t) > 0:
        if w[-1] <= t[-1]:
            sum += w[-1]
            w.pop(), t.pop()
            continue
        elif w[-1] > t[-1]:
            w.pop()
            continue
    print("#{} {}".format(test_case+1, sum))