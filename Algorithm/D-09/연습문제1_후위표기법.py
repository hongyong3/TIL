data = '2+3*4/5'
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
a = []
b = []
for i in data:
    if i in num:
        a.append(i)
    else:
        b.append(i)

for j in b[::-1]:
    a.append(j)
print(''.join(a))


str = "2+3*4/5"
stack = []

for i in range(len(str)):
    if str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
        stack.append(str[i])
    else:
        print(str[i], end="")

while len(stack) != 0:
    print(stack.pop(), end="")


str1 = '2+3*4/5'
stack1 = []

for i in str1:
    if i.isdigit():
        print(i, end='')
    else:
        stack1.append(i)

while stack1:
    print(stack1.pop(), end='')