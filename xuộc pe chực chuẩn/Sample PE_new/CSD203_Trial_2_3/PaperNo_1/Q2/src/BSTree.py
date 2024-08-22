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
    #end def
    
    def insert(self,name, price):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if name[0]=='B'or price>100:
            return
        
        new_node=Node(Car(name,price))
        if self.isEmpty():
            self.root = new_node
        else:
            current =self.root
            father =None
            while current is not None:
                if current.data.Price == price:
                    return
                father=current
                if current.data.Price <price: 
                    current=current.right
                else:
                    current=current.left
            if father.data.Price>price:
                father.left=new_node
            else:
                father.right=new_node
       
        
        #########################
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
        self.preVisit2()



        ####################
    def preOrder2(self,p):
        if p==None:
            return
        if 3<=p.data.Price<=5:
            self.visit(p)
        self.preOrder2(p.left)
        self.preOrder2(p.right)
    #end def
    def preVisit2(self):
        self.preOrder2(self.root)
        print("")
    
    pass
    
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        
        
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left is not None and p.right is not None and p.data.Price<7:
                self.delete_copy_left(p)
                return 
                
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        
        #############################

    def findNode(self,key):
        current=self.root
        while current is not None :
            if current.data.Price==key:
                return current
            elif current.data.Price<key:
                current=current.right
            else:
                current=current.left
        return None

    def delete_copy_left(self,node):
        deleteNode= node
        if deleteNode==None or deleteNode.left==None: 
            return 
        if deleteNode.left.right==None:     
            deleteNode.data=deleteNode.left.data
            deleteNode.left=deleteNode.left.left
        else:
            father=deleteNode.left
            current=deleteNode.left.right
            while current.right is not None: 
                father=current
                current=current.right
       
            deleteNode.data=current.data
            father.right=current.left
            
        pass
    def f4(self):
        #  ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left is not None and p.data.Price<7:
                self.rightRotation(p.data.Price)
                
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        #################################
        
    def finFather(self,key): 
        if self.root.data.Price==key: 
            return None
        current=self.root
        father=None
        while current:
            if current.data.Price==key:
                return father
            father=current
            if current.data.Price<key:
                current=current.right
            else:
                current=current.left
        if current: 
            return None
        

    def right_rotate(self,p):
        # kiểm tra node có none không 
        # kiểm tra có con trái không 
        if p==None or p.left==None:
            return 
        c= p.left
        p.left=c.right
        c.right=p
        return c

    def rightRotation(self,key):
        node=self.findNode(key)
        if node==None or node.left==None:
            return 
        father=self.finFather(key)
        if father==None:
            self.root=self.right_rotate(self.root)
        else:
            if father.data.Price<key:
                father.right=self.right_rotate(node)
            else:
                father.left=self.right_rotate(node)

# end class
