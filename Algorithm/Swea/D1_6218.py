import sys
sys.stdin = open("D1_6218_input.txt", "r")

a = int(input())
for i in range(1, a + 1):
    if a / i == a // i:
        print(str(i) + "(은)는", str(a) + "의 약수입니다.")