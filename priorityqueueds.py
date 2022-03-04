size=4
queue=[]
front=0

def push(priority,element):
    if len(queue)== 4:
        print("queue is full.")
    else:
        queue.append((priority,element))

def pop():
    global front
    if len(queue)==0:
        print("queue is empty")
    else:
        y=[]
        for i in queue:
            y.append(i[0])
        front=y.index(max(y))
        del queue[front]
push(1,"karan")
push(4,"parekh")
push(2,"arjun")
push(3,"soni")
print(queue)
push(5,"dharmit")
pop()
print(queue)
pop()
print(queue)
pop()
print(queue)
pop()
print(queue)
pop()










