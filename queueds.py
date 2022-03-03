size=4
queue=[None]*size
front=0
rear=0

def push(element):
    global rear
    if rear >= size:
        print('queue is full!')
    else:
        queue[rear]=element
        rear=rear+1

def pop():
    global rear
    global front
    if front == rear:
        print('queue is empty!')
    else:
        queue[front] = None
        front += 1

push(10)
push(20)
push(30)
push(40)
print(queue)
push(50)
pop()
pop()
pop()
pop()
print(queue)
pop()






