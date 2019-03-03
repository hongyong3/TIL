import sys
sys.stdin = open("숫자근_input.txt", "r")

def root_calc(num):
    while True:
        total = 0
        while num:
            total += num%10
            num //= 10
        if total < 10:
            return total
        num = total

T = int(input())
data = list(int(input()) for _ in range(T))
stack = []
max = 0
ans = 0

for i in range(T):
    root = root_calc(data[i])
    stack.append(root)
    for j in range(len(stack)):
        if max < stack[j]:
            max = stack[j]
            ans = data[j]
        if max == stack[j]:
            if ans > data[j]:
                ans = data[j]
print(ans)