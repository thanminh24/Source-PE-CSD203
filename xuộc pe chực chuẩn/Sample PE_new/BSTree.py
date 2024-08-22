from Car import *
from Node import *
class NodeQ:
    def __init__(self,data):
        self.data = data
        self.next = None
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def EnQueue(self, data):
        node = NodeQ(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    #end def
    def DeQueue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data
#end class    
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    def insert(self,name, price):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        newNode = Node(data = Car(name, price))
        if name[0] == "B" or  price > 100:
        # Sửa điều kiện theo đề bài yêu cầu
            return
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            while current:
                if price < current.data.Price:
                    if current.left:
                        current = current.left
                    else:
                        current.left = newNode
                    
                        break
                elif price > current.data.Price:
                    if current.right:
                        current = current.right
                    else:
                        current.right = newNode
                        
                        break
                else:
                     break
    
           pass
    #end def
    def visit(self,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    #end def
    def preOrder(self,p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    #end def
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    #end def
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    #end def
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    #end def
    def inOrder(self,p):
        if p==None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)        
    #end def
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    #end def
    def breadth_first(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")        
    #end def
    
    def f2(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        self.preOrder2(self.root)
        print("")
    def preOrder2(self, p):
    # đề yêu cầu thứ tự nào thì copy thứ tự đấy (ví dụ ở đây yêu cầu preOrder thì copy hàm preOrder cho trước ở phía trên rồi đổi tên)
        if p==None:
            return
        if p.data.Price <= 5 and p.data.Price >= 3:
        # Sửa điều kiện theo đề yêu cầu, điều kiện luôn đừng trước self.visit
            self.visit(p)
        self.preOrder2(p.left) #nhớ đổi tên
        self.preOrder2(p.right) #nhớ đổi tên
