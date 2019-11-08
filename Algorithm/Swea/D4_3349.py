import sys
sys.stdin = open("D4_3349_input.txt", "r")
def solve(x, y, n):
   global count, xy
   if x < xy[n][0] and y < xy[n][1]:
       if (xy[n][0] - x) == (xy[n][1] - y):
           count += (xy[n][0] - x)
       else:
           count += min(xy[n][0], xy[n][1]) - max(x, y) + max(xy[n][0], xy[n][1]) - min(x + min(xy[n][0], xy[n][1]) - max(x, y), y + min(xy[n][0], xy[n][1]) - max(x, y))
   elif (x != xy[n][0] and y == xy[n][1]) or (x == xy[n][0] and y != xy[n][1]):
       count += abs(max(xy[n][0], xy[n][1]) - min(x, y))
   elif (x < xy[n][0] and y > xy[n][1]) or (x > xy[n][0] and y < xy[n][1]):
       count += (abs(xy[n][0] - x)) + abs((y - xy[n][1]))
   elif x > xy[n][0] and y > xy[n][1]:
       if (xy[n][0] - x) == (xy[n][1] - y):
           count += (x - xy[n][0])
       else:
           count += min(x, y) - max(xy[n][0], xy[n][1]) + max(x - min(x, y) + max(xy[n][0], xy[n][1]), y - min(x, y) - max(xy[n][0], xy[n][1])) + min(xy[n][0], xy[n][1])
   return count
T = int(input())
for test_case in range(1):
   W, H, N = map(int, input().split())
   xy = [list(map(int, input().split())) for _ in range(N)]
   count = 0
   for i in range(N - 1):
       solve(xy[i][0], xy[i][1], i + 1)
   print("#{} {}".format(test_case + 1, count))