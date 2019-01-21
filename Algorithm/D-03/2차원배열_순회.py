array = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
# i : 행의 좌표, n = len(array)
# j : 열의 좌표, m = len(array[0])

# 행 우선

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end = " ")
    print()
print()

# 열 우선

for j in range(len(array[0])):
    for i in range(len(array)):
        print(array[i][j], end = " ")  # end = " "은 줄 바꿈을 안할려고
    print()
print()

# 지그재그 우선

for i in range(len(array)):
    for j in range(len(array[0])):
        print([i][j + (i- 1 -2*j) * (i%2)], end = " ")
    print()
print()