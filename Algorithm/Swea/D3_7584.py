import sys
sys.stdin = open("D3_7584_input.txt", "r")

# 다른 방법.. 점화식?
a = "001001100011011"
s = str.maketrans('01', '10')
cnt = 15
while cnt < 100000000:
    a = a + '0' + a[::- 1].translate(s)
    cnt = cnt * 2 + 1


T = int(input())
for test_case in range(T):
    N = int(input())
    cnt = 15
    memory = ["001", "0010011", "001001100011011"]