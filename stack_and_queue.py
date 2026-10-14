def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()
s = []
push(s, 10)
push(s, 20)
print(pop(s))

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    return queue.pop(0)
q = []
enqueue(q, 10)
enqueue(q, 20)
enqueue(q, 30)
print(dequeue(q))
print(q)