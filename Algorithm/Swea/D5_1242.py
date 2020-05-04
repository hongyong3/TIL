import sys
sys.stdin = open("D5_1242_input.txt", "r")

# 주어진 암호코드(16진수) => 2진수로 변환 -> binaryConversion
# 암호코드 패턴찾기.. 어떻게 하지? -> 규칙이 있을 듯

# 그렇게 변환된 암호(8자리; 7자리 암호 + 검증코드)
# (홀수자리 수 * 3 + 짝수자리 수 + 검증코드) % 10 == 0이면
# 올바른 암호가 되고, 변환된 암호를 모두 더한 값이 정답

# 16진수 -> 2진수 변환
# dict
binaryConversion = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
                    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
                    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
                    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

T = int(input())
for test_case in range(1):
    N, M = list(map(int, input().split()))
    data = [input() for _ in range(N)]
    binaryList = [''] * N

    # data 16진수 -> 2진수 변환
    for i in range(N):
        for j in range(M):
            binaryList[i] += binaryConversion[data[i][j]]