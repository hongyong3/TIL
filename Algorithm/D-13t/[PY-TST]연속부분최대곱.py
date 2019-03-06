import sys
sys.stdin = open("연속부분최대곱_input.txt", "r")
N = int(input())
data = tuple(float(input()) for i in range(N))
ans = [0] * N
ans[0] = data[0]
for i in range(1, N):
	if  data[i] < ans[i-1] * data[i]:
		ans[i] = ans[i-1] * data[i]
	else:
		ans[i] = data[i]
print("{:.3f}".format(max(ans)))