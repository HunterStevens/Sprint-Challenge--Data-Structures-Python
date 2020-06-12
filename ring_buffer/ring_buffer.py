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
            if type(item) == str:
                self.ring.pop(0)
                self.ring.insert(0, item)

                # for x in self.ring:
                #     self.tracker = x
                #     if chr(ord(item) -1) == self.tracker:
                #         self.ring.remove(x)

            else:
                test = item - 1
                for x in self.ring:
                    if test == self.ring.index(x):
                        print(self.ring)
                        self.ring.remove(x)
                        print(self.ring)
                        position = self.ring.index(x)
                        self.ring.insert(x, item)                        
                    else:
                        pass


    def get(self):
        queue = []
        for x in self.ring:
            queue.append(x)
        return queue