def push(item):
    s.append(item)
def pop():
    if len(s) == 0:
        print("Stack is empty!")
        return
    else:
        return s.pop(-1)

s = []

push(1)
push(3)
push(2)
print(pop())
print(pop())
print(pop())