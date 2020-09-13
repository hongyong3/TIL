import sys
sys.stdin = open("D3_3975_input.txt", "r")

T = int(input())
mat = []
for test_case in range(T):
    A, B, C, D = map(int, input().split())
    if abs((A / B)-(C / D)) <= 10e-7: mat.append('#{} {}'.format(test_case + 1, 'DRAW'))
    elif A / B > C / D: mat.append('#{} {}'.format(test_case + 1, 'ALICE'))
    else: mat.append('#{} {}'.format(test_case + 1, 'BOB'))
print('\n'.join(mat))