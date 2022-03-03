size=4
stack=[None]*size
top=-1

def push(element):
    global top
    top=top+1
    if top >= size:
        print('Stack overflow!')
        top=top-1
    else:
        stack[top]=element

def pop():
    global top
    if top==-1:
        print('Stack underflow!')
    else:
        stack[top] = None
        top -= 1

push(10)
push(20)
push(30)
push(40)
print(stack)
push(50)
push(60)
pop()
pop()
pop()
pop()
print(stack)
pop()




