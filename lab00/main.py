
class Stack:
    def __init__(self):
        self.items=[]
        self.items.append("stack first")
    def push(self,x):
        self.items.append(x)
    def pop(self):
        self.items.pop()
    def empty(self):
        return len(self.items)==0
    def sizeofstack(self):
        return len(self.items)

class FancyStack(Stack):
    def peek(self,n):
        size = len(self.items)
        return self.items[size-1-n]

x =Stack()
x.push(1)
x.push(2)
x.push(3)
x.push(4)
print(x.items)

y=FancyStack()
y.push("fancy")
print(y.items)
print(y.peek(1))