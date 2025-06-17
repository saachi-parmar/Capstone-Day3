print("\n")
#-----------------------------------------------------------------------------
# STACK - LIFO: Last in First Out --------------------------------------------
class stack:
    def __init__(self):
        self.value = []
    
    def push(self, x):                        # Last In
        self.value = [x] + self.value
        
    def pop(self):                            # First Out
        return self.value.pop(0)
    
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.value)
print(s.pop())
print(s.value)
s.push(50)
print(s.value)
print(s.pop())
print(s.value)


print("\n")

#------------------------------------------------------------------------------
# QUEUE - FIFO: First In First Out---------------------------------------------
class Queue:
    def __init__(self):
        self.values = []
        
    def enqueue(self, x):
        return self.values.append(x)
        
    def dequeue(self):
        if self.values:
            return self.values.pop(0)
        print("Queue is empty")
        return None

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Queue before dequeue: ", q.values)

dequeued_element = q.dequeue()
print("Dequeue element: ", dequeued_element)
print("Queue after dequeue: ", q.values)

q.enqueue(50)
print("Queue after enqueue: ", q.values)
q.dequeue()
print("Queue after dequeue: ", q.values)
q.dequeue()
print("Queue after dequeue: ", q.values)
q.dequeue()
print("Queue after dequeue: ", q.values)
q.dequeue()
print("Queue after dequeue: ", q.values)


print("\n")

