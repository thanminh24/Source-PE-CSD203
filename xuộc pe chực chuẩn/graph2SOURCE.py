class Person:
    def __init__(self, xType = "", xRate = 0, xWing = 0):
        self.xType = xType
        self.xRate = xRate
        self.xWing = xWing

    def __str__(self):
        return f"({ self.xType}, {self.xRate}, {self.xWing})"

class Node:
    def __init__(self, person, nx = None):
        self.info = person
        self.next = nx
        
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None
    
    def traverse(self):
        p = self.head
        while p:
            print(p.info, end=" ")
            p = p.next
        print()
    
    def addlast(self, newNode):
        if self.isEmpty():
            self.head = self.tail = newNode
        self.tail.next = newNode
        self.tail = newNode
        if self.tail == None:
            self.tail = newNode

    def f2(self, x, y):
        if self.isEmpty():
            return
        
        p = self.head
        count = 0
        while p:
            p = p.next
            count += 1
            if count == 3:
                x.next = p.next
                p.next = x
            if count == 5:
                y.next = p.next
                p.next = y
            return

    def f4(self):
        if self.isEmpty():
            return
        
        # find max
        p = self.head
        node_max = None
        while p:
            if node_max is None or node_max.info.xRate < p.info.xRate:
                node_max = p
            p = p.next

        p = self.head
        while p:
            q = p.next
            while q:
                if p.info.xRate > q.info.xRate:
                    p.info, q.info = q.info, p.info
                q = q.next
                if q.info == node_max.info:
                    break
            p = p.next
            if q.info == node_max.info:
                break
        
        p = node_max.next
        while p:
            q = p.next
            while q:
                if p.info.xRate > q.info.xRate:
                    p.info, q.info = q.info, p.info
                q = q.next
            p = p.next
        

myList = MyList()
types = ["A", "B", "C", "D", "E", "F", "G"]
rates = [2, 5, 6, 9, 7, 4, -3]
wings = [8, 3, 5, 4, 9, -7, 2]

for i in range(len(types)):
    myList.addlast(Node(Person(types[i], rates[i], wings[i])))

myList.traverse()

myList.f4()

myList.traverse()