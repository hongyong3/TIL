import sys
sys.stdin = open("2112_input.txt", "r")

# 최적화
# 다중 반복문에서 특정 위치로 이동하는 것이 필요. -> for-else 사용

from itertools import product, combinations
# 1. product : 복원 순열
# 2. permutation : (비복원) 순열
# 3. combinations_with_replacement : 복원 조합
# 4. combinations : (비복원) 조합

def solve():
    for cnt in range(K):    # 0 ~ K - 1
        for ab in product((0, 1), repeat=cnt):
            for idx in combinations(range(D), cnt):
                for line in zip(*data):
                    line = list(line)
                    for i in range(cnt):
                        line[idx[i]] = ab[i]
                    # 결과 확인
                    for y in range(D - K + 1):
                        temp = line[y]
                        for dy in range(1, K):
                            if temp != line[y + dy]:
                                break   # 조건 미충족, 다음 y 확인
                        else:
                            # 조건 충족, 다음 x 확인
                            break
                    else:
                        # 한 줄 전체가 조건 미충족, 다른 경우의 수 확인
                        break
                else:
                    # 모두 조건 충족, 결과 출력
                    return cnt
    # 최악의 경우
    return K

T = int(input())
for test_case in range(T):
    D, W, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(D)]
    print(data)
    print("#{} {}".format(test_case + 1, solve()))