import sys
sys.stdin = open("D1_6219_input.txt", "r")

a = int(input())
ans = []
for i in range(1, a + 1):
    if a / i == a // i:
        print(str(i) + "(은)는 " + str(a) + "의 약수입니다.")
        ans.append(str(i))
if len(ans) == 2:
    print(str(a) + "(은)는 " + ans[0] + "과 " + ans[1] + "로만 나눌 수 있는 소수입니다.")