import sys
sys.stdin = open("D6_3950_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     l = int(input())
#     s = input()
#     ans = []
#     cnt, temp = 0, 0
#     chk = True if s[0] == '(' else False    # True : '(', False : ')'
#
#     for i in range(l):
#         if chk:
#             if s[i] == '(':
#                 temp += 1
#             else:
#                 temp -= 1
#                 chk = False
#         else:
#             if s[i] == '(':
#                 ans.append((i, i + temp))
#                 chk = True
#             else:
#                 temp -= 1
#     print(ans)

T = int(input())
for test_case in range(1):
    l = int(input())
    a = input()
    cnt, ans = 0, []

    if l % 2:
        print("#{} {}".format(test_case + 1, - 1))
        continue

    if not a.count(')'):        # '('만 존재
        print("#{} {}".format(test_case + 1, 1))
        print(l // 2, l - 1)
        continue

    elif not a.count('('):      # ')'만 존재
        print("#{} {}".format(test_case + 1, 1))
        print(0, l // 2 - 1)
        continue
    # else:
    #     k = 0
    #     temp = 0
    #     while k < l - 1:
    #         if cnt == 10:
    #             print("#{} {}".format(test_case + 1, - 1))
    #             break
    #         s = a[k]
    #         if s == '(':
    #             temp = 0
    #             for i in range(k, l):
    #                 if s == a[i]:
    #                     temp += 1
    #                 else:
    #                     k = i
    #                     if temp > 0:
    #                         temp -= 1
    #                     else:
    #                         break
    #         else:
    #             temp -= 1
    #             for i in range(k, l):
    #                 if s == a[i]:
    #                     temp += 1
    #                 else:
    #                     cnt += 2
    #                     ans.append((k, k))
    #                     ans.append((i, i))
    #                     k = i + temp
    #                     break
    #     print("#{} {}".format(test_case + 1, cnt))
    #     for i in ans:
    #         print(*i)
    else:
        temp = 0
        chk = True if a[0] == '(' else False
        for i in range(l):
            if a[i] == '(':
                if chk:
                    temp += 1
                else:
                    if k + temp < 0:
                        ans.append((k, k))
                        ans.append((i, i))
                        cnt += 2
                    else:
                        ans.append((i, k + temp))
                        cnt += 1
            else:
                if not chk:
                    k = i
                    temp -= 1
                else:
                    temp -= 1
                    chk = False
                    k = i