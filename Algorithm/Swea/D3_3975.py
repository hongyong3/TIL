import sys
sys.stdin = open("D3_3975_input.txt", "r")

T = int(input())
ans = []
for test_case in range(T):
    A, B, C, D = map(int, input().split())
    if abs((A / B)-(C / D)) <= 10e-7: ans.append('#{} {}'.format(test_case + 1,'DRAW'))
    elif A / B > C / D: ans.append('#{} {}'.format(test_case + 1,'ALICE'))
    else: ans.append('#{} {}'.format(test_case + 1,'BOB'))
<<<<<<< HEAD
    # ans.append('#{} {}'.format(test_case + 1,'ALICE') if A / B > C / D else '#{} {}'.format(test_case + 1,'DRAW') if abs((A / B)-(C / D)) <= 10e-7 else '#{} {}'.format(test_case + 1,'BOB'))
=======
>>>>>>> acfb0f955d879cf7f497c0be2ffd446db2f83ed7
print('\n'.join(ans))