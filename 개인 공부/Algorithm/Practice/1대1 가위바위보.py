import sys
sys.stdin = open("1대1 가위바위보_input.txt", "r")

data = list(map(int, input().split()))
# if A == 1 and B == 2:
#     print('B')
# elif A == 1 and B == 3:
#     print('A')
# elif A == 2 and B == 3:
#     print('B')
# elif A == 2 and B == 1:
#     print('A')
# elif A == 3 and B == 1:
#     print('B')
# elif A == 3 and B == 2:
#     print('A')
# elif A == B:
#     print('B')

if data[0] < data[1] or data[0] ==data[1]:
    print('B')
else:
    print('A')