import sys
sys.stdin = open("원안의 사각형_input.txt", "r")

R  =
count = 0
for i in range(1, R):
    for j in range(1, R):
        if R**2 >= i**2 + j**2:
            count += 1
print(count*4)