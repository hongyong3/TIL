import sys
sys.stdin = open("D4_2983_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = input()
    commonWord, toWord, LongestNum = "", "", 0

    for i in data:
        if commonWord + i in toWord:
            commonWord += i
            toWord += i
            continue
        else:
            if LongestNum < len(commonWord):
                LongestNum = len(commonWord)

            if i in toWord:
                commonWord = i
            else:
                commonWord = ""
            toWord += i

    if LongestNum < len(commonWord):
        LongestNum = len(commonWord)

    print("#{} {}".format(test_case + 1, LongestNum))