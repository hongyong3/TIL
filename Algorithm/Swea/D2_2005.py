import sys
sys.stdin =open("D2_2005_input.txt", "r")
import  math

def combination(i, j):
    return int(math.factorial(i) / (math.factorial(j) * math.factorial(i - j)))

def pascals_triangle(N):
    result = []
    for i in range(N):
        row = []
        for j in range(i + 1):
            row.append(combination(i, j))
        result.append(row)
    return result

T =int(input())
for test_case in range(T):
    N = int(input())
    print("#{}".format(test_case+1))
    for row in pascals_triangle(N):
        print(*row)