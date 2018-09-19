#Ulysses Atkeson, 9/19/28, implement a Queue using stacks
class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = []
        self.pointer.append(pointer)
    def getData(self):#returns data object
        return(self.data)
    def changeData(self, newData):#changes data to newData
        self.data = newData
    def addPoint(self, newNode):#adds newNode to the end of the pointer array
        self.pointer.append(newNode)
    def addPointAtIndex(self, newNode, index):#adds newNode to the end of the pointer array
        self.pointer[index] = newNode
    def rmPoint(self, index):#removes pointer at index in array
        if(index < len(self.pointer)):
            del self.pointer[index]
    def setPoint(self, index, node):#sets pointer at index in array
        self.pointer[index] = node
    def getNode(self, index):#returns pointer at index
        if(index < len(self.pointer)):
            return self.pointer[index]
    def pointerCount(self):
        return len(self.pointer)
    def hasPointer(self):
        if self.pointer == None:
            return 0
        return 1
    def __repr__(self):
        first = 'None'
        if self.pointer[0] != None:
            first = self.pointer[0].data
        return "{data:"+str(self.data)+", pointers:"+str(self.pointerCount())+", First Pointer's Data:"+str(first)+"}"

class Stack:
    def __init__(self):
        self.top = None
        self.sizeNum = 0
    def push(self, data):
        self.top = Node(data, self.top)#Set top to a new node with a pointer to the old top
        self.sizeNum = self.sizeNum + 1
    def pop(self):
        if self.top != None:#if there is data
            temp = self.top.getData()#you are going to get rid of top so save its data
            if self.top.hasPointer() != 0:#if the new top will not be None
                self.top = self.top.getNode(0)#set new top to one node down
            else:#if the new top will be None
                self.top = None
            self.sizeNum = self.sizeNum - 1
            return(temp)
        else:
            return(None)
    def peek(self):
        if self.top == None:#if there is not data
            return None
        return(self.top.getData())
    def size(self):
        return self.sizeNum
    def isEmpty(self):
        if self.sizeNum == 0:
            return True
        return False

class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()
    def enqueue(self, data):#put onto inbox
        self.inbox.push(data)
    def dequeue(self):#if outbox is empty then flip onto outbox then pop
        if self.outbox.isEmpty():
            while not self.inbox.isEmpty():
                self.outbox.push(self.inbox.pop())
        if not self.outbox.isEmpty():
            return self.outbox.pop()
        else:
            return None
    def peek(self): #same as deque but use peek rather than pop
        if self.outbox.isEmpty():
            while not self.inbox.isEmpty():
                self.outbox.push(self.inbox.pop())
        if not self.outbox.isEmpty():
            return self.outbox.peek()
        else:
            return None
    def isEmpty(self): #if both stacks are empty
        return self.outbox.isEmpty() and self.inbox.isEmpty()
    def size(self):#add the sizes of the 2 stacks
        return self.outbox.size() + self.inbox.size()



queue1 = Queue()
print(queue1.size())#0
print(queue1.isEmpty())#Ture
queue1.enqueue("a")
print(queue1.size())#1
print(queue1.isEmpty())#False
print(queue1.dequeue())#a
print(queue1.dequeue())#None
print(queue1.isEmpty())#Ture
queue1.enqueue("b")
queue1.enqueue("c")
queue1.enqueue("d")
print(queue1.dequeue())#b
print(queue1.dequeue())#c
print(queue1.dequeue())#d
