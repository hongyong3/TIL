import sys
sys.stdin = open("D1_6319_input.txt", "r")

def palindrome(seq):
    ans = 0
    pal = [[0] * len(seq) for _ in range(len(seq))]
    for i in range(len(seq)):
        for j in range(len(seq) - i):
            if i < 2 and seq[j] == seq[i + j] or seq[j] == seq[i + j] and pal[j + 1][i + j - 1]:
                pal[j][i + j] = 1
                ans = i + 1
    if ans == len(seq):
        print(seq)
        print("입력하신 단어는 회문(Palindrome)입니다.")

    # if seq == seq[:: - 1]:
    #     print(seq)
    #     print("입력하신 단어는 회문(Palindrome)입니다.")

seq = input()
palindrome(seq)