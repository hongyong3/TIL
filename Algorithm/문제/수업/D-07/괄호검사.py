'''
()()((()))
((()((((()()((()())((())))))
'''

def push(item):
    s.append(item)
def pop():
    if len(s) == 0:
        print("Stack is empty!")
        return
    else:
        return s.pop(-1)

def isEmpty():
    if lens(s) == 0:
        return True
    else:
        return False

def check_matching(data):
    for i in range(len(data)):
        if data[i] == "(":
            push(data[i])
        elif data[i] == ")":
            if isEmpty():
                return False
            pop()
    if not isEmpty():
        return False
    else:
        return True

data = input()
print(check_matching(data))

push(1)
push(3)
push(2)
print(pop())
print(pop())
print(pop())