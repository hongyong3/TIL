import sys
sys.stdin = open("D4_15869_input.txt", "r")

'''
올바른 괄호 문자열은 아래와 같이 정의된다.

1. 빈 문자열은 괄호 문자열이다.
2. S가 괄호 문자열일때, (S)도 괄호 문자열이다.
3. S와 T가 괄호 문자열이라면, ST도 괄호 문자열이다.
4. 모든 괄호 문자열은 위의 3개 규칙으로만 만들 수 있다.

예를 들어 “”, “()”, “(()())()”은 올바른 괄호 문자열이지만, “hi”, “)(“, “((())()”는 올바른 괄호 문자열이 아니다.

짝수인 정수 n과 k가 주어질 때, 길이가 n인 올바른 괄호 문자열 중 연속한 k개의 문자를 어떻게 잡더라도 올바른 괄호 문자열이 아닌 것이 존재하는지 판단하고, 존재한다면 아무거나 하나 출력하는 프로그램을 작성하라.
'''
# 75 // 4310 Fail
# T = int(input())
# for test_case in range(T):
#     N, M = map(int, input().split())
#     if N - M >= 2:
#         ans = '()' * (N // 2)
#     else:
#         ans = - 1
#     print("#{} {}".format(test_case + 1, ans))

# 156 / 4310 Fail
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    if N % M:
        ans = '()' * (N // 2)
    else:
        ans = - 1
    print("#{} {}".format(test_case + 1, ans))