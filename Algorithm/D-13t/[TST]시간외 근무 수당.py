import sys
sys.stdin = open("시간외 근무 수당_input.txt", "r")
time = []
a = 0
for test_case in range(5):
    s, e = list(map(float, input().split()))
    time.append((s, e))
for i in range(5):
    if 1 < time[i][1] - time[i][0] <= 4:
        a += (time[i][1] - time[i][0] - 1)
    elif 5 > time[i][1] - time[i][0] > 4:
        a += (time[i][1] - time[i][0] - 1)
    elif time[i][1] - time[i][0] >= 5:
        a += 4
    else:
        pass

if a >= 15:
    print(int(a*(10000-500)))
elif a <= 5:
    print(int(a*(10000+500)))
else:
    print(int(a*10000))