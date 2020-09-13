import sys
sys.stdin = open("D1_6219_input.txt", "r")

a = int(input())
mat = []
for i in range(1, a + 1):
    if a / i == a // i:
        print(str(i) + "(은)는 " + str(a) + "의 약수입니다.")
        mat.append(str(i))
if len(mat) == 2:
    print(str(a) + "(은)는 " + mat[0] + "과 " + mat[1] + "로만 나눌 수 있는 소수입니다.")