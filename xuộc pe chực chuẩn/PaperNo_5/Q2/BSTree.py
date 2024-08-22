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
    def f1(self, name, age, salary=-1):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        newNode = Node(Employee(name, age,salary))
        if name.startswith("Y") or  age < 0 or salary <= 0:
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
        
        
        pass     
    def f2(self):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2========
        self.postOrder2(self.root)
        print("")
        
    def postOrder2(self,p):
        if p==None:
            return
        self.postOrder2(p.left)
        self.postOrder2(p.right)
        if p.data.Age % 2 == 0 and p.data.Salary > 20:
            self.visit(p)


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
            if count == 2: #sửa theo đề bài
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
        pass
    
    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========      
        p = self.search_f4()
        self.rotate_right(p)
    
    def search_f4(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.data.Age % 2 != 0 :
            #Sửa điều kiện theo yêu cầu đề bài
                count += 1
            if count == 1:
            # Đề yêu cầu là node thứ mấy thì count bằng bấy nhiêu (ví dụ đề yêu cầu 'first node' thì count = 1
                return p
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        return None
    
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Age < root.data.Age:
        #Sửa data. theo yêu cầu đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
    def rotate_right(self, node):
        if not node:                                            
            return None
        left_node = node.left                                   
        if not left_node:                                       
            return node
        left_right_node = left_node.right
        node.left = left_right_node                             
        left_node.right = node
        if node == self.root:                                   
            self.root = left_node
        else:                                                   
            parent = self._find_parent(self.root, node)         
            if parent.left == node:                             
                parent.left = left_node
            else:                                               
                parent.right = left_node
        return left_node
        pass         
    #-----------------     
    
# end class
