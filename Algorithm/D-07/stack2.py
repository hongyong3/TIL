SIZE = 100
stack = [0]* SIZE
top = -1
def push(item):
    global top
    if top > SIZE -1:
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top
    if top == -1:
        print("Stack is Empty!")
        return 0;
    else:
        result = stack[top]
        top -= 1
        return result

push(12)
push(44)
push(5888)
print(pop())
print(pop())
print(pop())
# print(top, stack)
