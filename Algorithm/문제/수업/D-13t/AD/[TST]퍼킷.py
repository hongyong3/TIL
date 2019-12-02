import sys
sys.stdin = open("[TST]퍼킷_input.txt", "r")

def flavor(s, sour, bitter):    # sour 곱이므로 1  bitter 합이므로 0
    global minn
    if s == N:
        if sour == 1 and bitter == 0:   # 요소가 아무것도 없을때도 차이는 1이므로 이 경우 제외
            return
        else:
            gap = abs(sour - bitter)
            if gap < minn:
                minn = gap
            return

    flavor(s + 1, sour, bitter)
    flavor(s + 1, sour * data[s][0], bitter + data[s][1])

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
minn = float('inf')
flavor(0, 1, 0)
print(minn)