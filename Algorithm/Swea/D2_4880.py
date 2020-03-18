import sys
sys.stdin = open("D2_4880_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    people = {}
    for i in range(N):
        people[i + 1] = data[i]
    print(people)