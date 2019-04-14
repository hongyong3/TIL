import sys
sys.stdin = open("패턴 마디의 길이_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = input()
    count = 0
    for i in range(1, len(data)):
        ans = data[0:i]
        answer = len(ans)
        if data[answer : 2 * answer] == ans:
            count = answer
            break
    print("#{} {}".format(test_case+1, count))