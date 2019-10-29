import sys
sys.stdin = open("D4_4366_input.txt", "r")

T = int(input())
for test_case in range(T):
    binary, ternary, binary_list, ternary_list = str(input()), str(input()), [], []

    for i in range(len(binary)):
        binary2 = list(binary)
        if binary2[i] == "0":
            binary2[i] = "1"
            binary_list.append(int(''.join(binary2), 2))
        else:
            binary2[i] = "0"
            binary_list.append(int(''.join(binary2), 2))

    for i in range(len(ternary)):
        ternary2 = list(ternary)
        if ternary2[i] == "0":
            ternary2[i] = "1"
            ternary_list.append(int(''.join(ternary2), 3))
            ternary2[i] = "2"
            ternary_list.append(int(''.join(ternary2), 3))
        elif ternary2[i] == "1":
            ternary2[i] = "0"
            ternary_list.append(int(''.join(ternary2), 3))
            ternary2[i] = "2"
            ternary_list.append(int(''.join(ternary2), 3))
        else:
            ternary2[i] = "0"
            ternary_list.append(int(''.join(ternary2), 3))
            ternary2[i] = "1"
            ternary_list.append(int(''.join(ternary2), 3))
    print("#{} {}".format(test_case + 1, *list(set(binary_list) & set(ternary_list))))