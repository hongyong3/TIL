import sys
sys.stdin = open("D3_7675_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = input().replace('!',' !').replace('.',' .').replace('?',' ?').split()
    count = 0
    res = ''
    for i in data:
        if i.isalpha() and i == i.capitalize():
            count += 1
        if i in '.!?':
            res += str(count) + ' '
            count = 0
    print("#{} {}".format(test_case + 1, res))

T = int(input())

for test_case in range(1, T + 1):
    num_corpus = int(input())
    corpus = input() + ' '
    corpus = corpus.replace('!', '.').replace('?', '.').split('. ')
    answer = '#{}'.format(test_case)
    for cor in corpus[:-1]:
        count = 0
        for word in cor.split(' '):
            if (word[0] == min(word)) and (word[0].isupper() == True) and(word[1:].lower() == word[1:]): # idea: 조건
                count +=1
        answer += ' {}'.format(count)
    print(answer)
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     data = list(map(str, input().split()))
#     ans = [0] * N
#     k = 0
#     for i in range(len(data)):
#         if data[i].isalpha() and data[i][0].isupper():
#             if len(data[i]) == 1:
#                 ans[k] == 1
#             else:
#                 if data[i][1:].islower():
#                     ans[k] += 1
#                     continue
#         if data[i][0].isupper() and (data[i][-1] == "." or data[i][-1] == "?" or data[i][-1] == "!"):
#             if data[i][1: -1].isalpha():
#                 if not data[i][1: -1].isupper() and data[i][1: -1].islower():
#                     ans[k] += 1
#                     k += 1
#             else:
#                 k += 1
#     print("#{} ".format(test_case + 1), end="")
#     print(*ans)