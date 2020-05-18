import time

a = time.time()


class Queue:

    def __init__(self, data):
        self.queue = list()
        self.maxsize = data
        self.head, self.tail = 0, 0

    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        else:
            return self.maxsize - (self.head - self.tail)

    def enqueue(self, data):
        if self.size() == (self.maxsize - 1):
            print("queue is full")
        else:
            self.queue.append(data)
            self.tail = (self.tail + 1) % self.maxsize
            return True

    def dequeue(self):
        if self.size() == 0:
            print("queue is empty")
        else:
            data = self.queue[self.head]
            self.head = (self.head + 1) % self.maxsize
            return data


q = Queue(int(10))
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.enqueue(50))
print(q.enqueue('Studytonight'))
print(q.enqueue(70))
print(q.enqueue(80))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
b = time.time()
print("---%.30f secends---" % (b-a))
