# 내 풀이

# array = [[1, 1, 1, 1, 1],
#          [1, 0, 0, 0, 1],
#          [1, 0, 0, 0, 1],
#          [1, 0, 0, 0, 1],
#          [1, 1, 1, 1, 1]]
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# for x in range(len(array)):
#     for y in range(len(array[x])):
#         for i in range(4):
#
#             testX = x - dx[i]
#             if testX > 0:
#                 testX = testX
#                 return testX
#             else:
#                 testX = -testX
#                 return testX
#             testY = y - dx[i]
#             if testY > 0:
#                 testY = testY
#                 return testY
#             else:
#                 testY = -testY
#                 return testY

# 선생님 풀이

'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''

def isWall(x, y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    return False

def calAbs(y, x):
    if y -x > 0:
        return y - x
    else:
        return x - y

arr = [[0 for _ in range(5)] for _ in range(5)] # [ ] 안이 열 // 바깥쪽이 행
for i in range(5):
    arr[i] = list(map(int, input().split()))
print(arr)

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# sum = 0
# for x in range(len(arr)):
#     for y in range(len(arr[x])):
#         for i in range(4):
#             testX = x + dx[i]
#             testY = y + dy[i]
#             if isWall(testX, testY) == False: # testX, testY가 0,0 같이 벽에 붙어 있지 않다면
#                 sum += calAbs(arr[y][x], arr[testY][testX])
# print("sum = {}".format(sum))