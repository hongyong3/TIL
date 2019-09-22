import sys
sys.stdin = open("Line_test1_input.txt", "r")

def consumer(data):
    global c_list
    for i in range(len(c_list)):
        j = 0
        if len(data) >= 1:
            c_list[i][0] += data[j]
            del (data[j])
        else: return
    c_list = sorted(c_list)
    consumer(data)

M, C = map(int, input().split())
data, c_list = [], [[0] for _ in range(C)]
for i in range(M):
    data.append(int(input()))
consumer(data)
print(*c_list[0])