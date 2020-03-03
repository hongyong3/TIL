import sys
sys.stdin = open("D1_6243_input.txt", "r")

# data = ','.join(sorted(list(set(list(map(str, input().split()))))))
# print(data)
print(','.join(sorted(list(set(list(map(str, input().split())))))))