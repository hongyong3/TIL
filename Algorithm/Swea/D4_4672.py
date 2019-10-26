import sys
sys.stdin = open("D4_4672_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = input()
    count, alphabet, cal = 0, [0] * 26, [0] * 11
    for i in data:
        alphabet[ord(i) - ord('a')] += 1
    for i in range(11):
        cal[i] = cal[i - 1] + i
    for i in alphabet:
        count += cal[i]
    print("#{} {}".format(test_case + 1, count))