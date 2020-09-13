import sys
sys.stdin = open("D5_1242_input.txt", "r")

# 주어진 암호코드(16진수) => 2진수로 변환 -> binaryConversion v

# 암호코드 패턴찾기.. 어떻게 하지? -> 규칙이 있을 듯 v
# 암호코드 type : dict
# 7칸이고 x:y:z:k 비율의 비율을 가짐.
# 여기서 실질적으로 쓰는 것은 y, z, k이고, 뒤에서부터 읽기.

# 그렇게 변환된 암호(8자리; 7자리 암호 + 검증코드) v
# (홀수자리 수 * 3 + 짝수자리 수 + 검증코드) % 10 == 0이면
# 줄이 여러개이므로 결과값의 중복을 피하기위해 visited 사용
# 올바른 암호가 되고, 변환된 암호를 모두 더한 값이 정답

# 16진수 -> 2진수 변환 type : dict
conversion = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
                    '4': "0100", '5': "0101", '6': "0110", '7': "0111",
                    '8': "1000", '9': "1001", 'A': "1010", 'B':"1011",
                    'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}

# 암호코드 type : dict
# 7칸이고 x:y:z:k 비율의 비율을 가짐.
# 여기서 실질적으로 쓰는 것은 y, z, k이고, 뒤에서부터 읽기.
decryption = {"211": 0, "221": 1, "122": 2, "411" : 3, "132": 4,
              "231": 5, "114": 6, "312": 7, "213": 8, "112": 9}

# 비율 최소화
def reduce(y, z, k):
    minValue = min(y, z, k)
    y //= minValue
    z //= minValue
    k //= minValue
    return str(y) + str(z) + str(k)


T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    data = [input() for _ in range(N)]
    binaryList = [''] * N   # 변환된 2진수를 담는 list
    temp = []   # 해독한 코드를 담는 list
    mat = 0
    visited = []    # 중복방지

    # data 16진수 -> 2진수 변환
    for i in range(N):
        for j in range(M):
            binaryList[i] += conversion[data[i][j]]

    for i in range(N):
        y, z, k = 0, 0, 0   # y = 1, z = 0, k = 1
        for j in range(M * 4 - 1, - 1, - 1):    # 변환된 2진수를 뒤에서 읽기
            # y:z:k의 비율을 저장
            if binaryList[i][j] == '1' and y == 0 and z == 0:
                k += 1
            elif binaryList[i][j] == '0' and y == 0 and k > 0:
                z += 1
            elif binaryList[i][j] == '1' and z > 0 and k > 0:
                y += 1

            if binaryList[i][j] == '0' and y > 0 and z > 0 and k > 0:
                temp.append(decryption[reduce(y, z, k)])
                y, z, k = 0, 0, 0

            if len(temp) == 8:
                temp = temp[:: - 1]
                value = (temp[0] + temp[2] + temp[4] + temp[6]) * 3 + temp[1] + temp[3] + temp[5] + temp[7]

                if value % 10 == 0 and temp not in visited:
                    mat += sum(temp)
                visited.append(temp)
                temp = []
                break

    print("#{} {}".format(test_case + 1, mat))