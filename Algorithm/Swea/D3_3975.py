import sys
sys.stdin = open("D3_3975_input.txt", "r")

T = int(input())
ans = []
for test_case in range(T):
    A, B, C, D = map(int, input().split())
    if abs((A / B)-(C / D)) <= 10e-7: ans.append('#{} {}'.format(test_case + 1,'DRAW'))
    elif A / B > C / D: ans.append('#{} {}'.format(test_case + 1,'ALICE'))
    else: ans.append('#{} {}'.format(test_case + 1,'BOB'))
print('\n'.join(ans))