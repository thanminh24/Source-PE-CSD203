import math
from Employee import *
from Node import *
from MyQueue import *
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
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
    def f1(self,name, age, salary=-1):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        newNode = Node(Employee(name, age, salary))
        if name.endswith("X") or  age > 100 or salary >= 100:
        # Sửa điều kiện theo đề bài yêu cầu
            return
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            while current:
                if age < current.data.Age:
                    if current.left:
                        current = current.left
                    else:
                        current.left = newNode
                    
                        break
                elif age > current.data.Age:
                    if current.right:
                        current = current.right
                    else:
                        current.right = newNode
                        
                        break
                else:
                     break   
    def f2(self):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2========
        


        pass    
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========
        p= self.pre_order_traversal(self.root)
        self.delete_merging_left(p.data.Age)

    def pre_order_traversal(self ,node):
        if node is None:
            return
        count = 0
        del_val = ''
        stack = []
        stack.append(node)

        while stack:
            current = stack.pop()
            if current.left is not None and current.right is not None and current.data.Age%2!=0: #sửa theo đề bài
                del_val = current
                count += 1
            if count == 1: #sửa theo đề bài
                return del_val

            # Right child is pushed first so that left is processed first
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
    
    def findNode(self,key):
        current=self.root
        while current is not None :
            if current.data.Age==key:
                return current
            elif current.data.Age<key:
                current=current.right
            else:
                current=current.left
        return None

    def finFather(self,key): # sử dụng trong merging 
        if self.root.data.Age==key: # trường hợp gốc là node cần xóa 
            return None
        current=self.root
        father=None
        while current:
            if current.data.Age==key:
                return father
            father=current
            if current.data.Age<key:
                current=current.right
            else:
                current=current.left
        if current: # không tồn tại key cần xóa trong cây 
            return None 

    def delete_merging_left(self,key): # lấy cụm con bên phải thành con phải của con ngoài cùng bên trái 
        delNode=self.findNode(key)
        if delNode==None or delNode.left is None:  # trường hợp node xóa không có con
            return
        father=self.finFather(key) 
        leftNode=delNode.left
        while(leftNode.right): 
            leftNode=leftNode.right
        leftNode.right=delNode.right
        if father is None:                          # trường hợp node cần xóa là node gốc
            self.root=self.root.left
        else:
            if father.left.data.Age<key:
                father.right=delNode.left
            else:
                father.left=delNode.left
        
    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========      
        



        pass         
    #-----------------     
    
# end class
