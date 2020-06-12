from collections import deque
class RingBuffer:
    def __init__(self, capacity):
        self.ring = []
        self.tracker = 0
        self.capacity = capacity
        pass

    def append(self, item):
        if self.capacity > 0:
            self.ring.append(item)
            self.capacity -= 1
        
        else:
            if self.tracker == 5:
                self.tracker = 0
                self.ring.pop(self.tracker)
                print(self.ring)
                self.ring.insert(self.tracker, item)
                print(self.ring)
                print("fired if statement")
            else:
                self.ring.pop(self.tracker)
                print(self.ring)
                self.ring.insert(self.tracker, item)
                print(self.ring)
                self.tracker += 1
                print("fired else statement")



    def get(self):
        queue = []
        for x in self.ring:
            queue.append(x)
        return queue