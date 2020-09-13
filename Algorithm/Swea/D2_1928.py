import sys
sys.stdin = open("D2_1928_input.txt", "r")

# encoding = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
#             "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
#             "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+",
#             "/"]
encoding = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

T = int(input())
for test_case in range(T):
    data = input()
    mat = ''
    for i in range(0, len(data), 4):
        idx1 = encoding.index(data[i])              # base64_encoding
        idx2 = encoding.index(data[i + 1])
        idx3 = encoding.index(data[i + 2])
        idx4 = encoding.index(data[i + 3])
        a = int(idx1 * 4) + int(idx2 / 16)          # base64_decoder
        b = int(idx2 % 16) * 16 + int(idx3 / 4)
        c = int(idx3 % 4) * 64 + int(idx4)
        mat += chr(a) + chr(b) + chr(c)        # combination
    print("#{} {}".format(test_case + 1, mat))