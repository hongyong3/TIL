import sys
sys.stdin = open("[TEST] 상자 포장하기_input.txt", "r")

def DFS(no, abox, bbox, apast, bpast):
    global ans


    if no >= N:
        sums = abox + bbox
        if ans < sums:
            ans = sums
        return

    if boxes[no] < apast:
        DFS(no+1, abox + boxes[no], bbox, boxes[no], bpast)
    if boxes[no] > bpast:
        DFS(no + 1, abox, bbox + boxes[no], apast, boxes[no])
    DFS(no + 1, abox, bbox, apast, bpast)


T = int(input())
for test_case in range(T):
    N = int(input())
    boxes = list(map(int, input().split()))
    ans = 0
    DFS(0, 0, 0, 1000, 0)
    print(ans)