import sys
sys.stdin = open("D4_10762_input.txt", "r")

'''
동원이 / 동생
1. 사탕 봉지를 뜯을 수 없다.
2. 둘 다 사탕 한 봉지 씩 가져야 한다.
3. 사탕을 공평하게 나누기를 원한다. 즉 동원이의 사탕의 개수의 합과 동생의 사탕 개수의 합이 같아야 한다.
4. 동생의 기준에서, 동원이가 가진 사탕 수 합은 동생의 사탕 수 합과 같아야 한다.
5. 단, 동생은 받아올림을 못 하기 때문에 두 수의 합을 bitwise XOR로 계산한다.
'''

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = "NO"
    data = list(map(int, input().split()))
    A, B = [], []
    for i in range()
