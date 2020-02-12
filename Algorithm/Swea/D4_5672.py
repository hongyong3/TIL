import sys
sys.stdin = open("D4_5672_input.txt", "r")

temporary = input()
T = ''
for t in temporary:
    if t.isdigit():
        T += t
for test_case in range(int(T)):
    temporary = input()
    N = ''
    for t in temporary:
        if t.isdigit():
            N += t
    data = [ord(input()[0]) for _ in range(int(N))]
    newData = ''
    print(data)

    front, back = 0, N - 1
    while front != back:
        newFront, newBack = front, back

        if data[front] < data[back]:
            newData += chr(data[front])
            newFront += 1

        elif data[front] > data[back]:
            newData += chr(data[back])
            newBack -= 1

        elif data[front] == data[back]:
            subFront = front + 1
            subBack = back - 1
            same, different = False, False

            while True:
                if data[subFront] != data[subBack]:
                    different = True
                    break
                else:
                    if subFront + 1 <= subBack - 1:
                        subFront += 1
                        subBack -= 1
                    else:
                        same = True
                        break

            # if same == False:
            #     if data[subFront] < data[subBack]:


    print("#{} {}".format(test_case + 1, newData))