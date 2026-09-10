from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            raise IndexError('Queue is empty')
        return self.items.popleft()

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    print(q.dequeue())
    print('Size:', q.size())
