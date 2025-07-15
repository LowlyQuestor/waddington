# Helper class and functions for init.py
class stack:
    def __init__(self):
        self.mem = []
    def push(self, item):
        self.mem.append(item)
    def pop(self):
        return self.mem.pop()
    def peek(self):
        if not self.mem:
            return []
        else:
            return self.mem[-1]
    def size(self):
        return len(self.mem)
    def look(self):
        print(self.mem)


