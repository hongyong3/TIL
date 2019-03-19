import sys
sys.stdin =open("정식이의 은행업무_input.txt", "r")
T = int(input())
for test_case in range(T):
    data2 = list(input())
    data3 = list(input())
    # print(data2, data3)

    for i in range(len(data2)):
        for j in range(len(data3)):
            if data2[i] == '0':
                data2[i] = '1'
                if data3[j] == '0':
                    data3[j] = '1'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '2'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '0'
                elif data3[j] == '1':
                    data3[j] = '0'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '2'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] ='1'
                elif data3[j] == '2':
                    data3[j] = '0'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '1'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '2'
                data2[i] = '0'

            elif data2[i] == '1':
                data2[i] = '0'
                if data3[j] == '0':
                    data3[j] = '1'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '2'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '0'
                elif data3[j] == '1':
                    data3[j] = '0'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '2'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '1'
                elif data3[j] == '2':
                    data3[j] = '0'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '1'
                    if int(''.join(data2), 2) == int(''.join(data3), 3):
                        print("#{} {}".format(test_case+1, int(''.join(data2), 2)))
                    data3[j] = '2'
                data2[i] = '1'