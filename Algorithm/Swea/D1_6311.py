import sys
sys.stdin = open("D1_6311_input.txt", "r")

data = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'
# score = 0
# score = data.count('A') * 4 + data.count('B') * 3 + data.count('C') * 2 + data.count('D') * 1
print((lambda a, b, c, d : a + b + c + d)(data.count('A') * 4, data.count('B') * 3, data.count('C') * 2, data.count('D') * 1))
print(type('1'))