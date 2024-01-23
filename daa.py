class StackArray:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, data):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        data = self.stack[self.top]
        self.top -= 1
        return data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]





class QueueArray:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data



opt=input("Enter 1 if you wnat to implement stack and queue using array or \nEnter 2 if you want to enter stack and queue using linked list:")
if(opt=='1'):
    stack_array = StackArray(5)
    stack_array.push(11)
    stack_array.push(24)
    stack_array.push(67)
    print("Top element:", stack_array.peek())
    print("Popped element:", stack_array.pop())
elif(opt=='2'):
    queue_array = QueueArray(5)
    queue_array.enqueue(87)
    queue_array.enqueue(54)
    queue_array.enqueue(13)
    print("Dequeued element:", queue_array.dequeue())
else:
    print("Invalid Input!!")
