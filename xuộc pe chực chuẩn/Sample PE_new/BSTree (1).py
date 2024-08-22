import math
from Node import *
from MyQueue import *

class Car:
    def __init__(self, name="", price=-1):
        self.Name = name
        self.Price = price
    def __repr__(self):
        return f"({self.Name},{self.Price})" 

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
    def f1(self,name, price):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if (name[0] == "B" or price > 100): # Sửa điều kiện theo đề bài yêu cầu
            return
        node = Node(Car(name, price)) # Sửa điều kiện theo đề bài yêu cầu
        if self.isEmpty():
            self.root = node
        else:
            cur = self.root
            father = None
            while cur:
                if cur.data.Price == price: # Sửa điều kiện theo đề bài yêu cầu
                    return
                father = cur
                if cur.data.Price < price: # Sửa điều kiện theo đề bài yêu cầu
                    cur = cur.right
                else:
                    cur = cur.left
            if father.data.Price > price: # Sửa điều kiện theo đề bài yêu cầu
                father.left = node
            else:
                father.right = node
        pass
    
    def f2(self):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2========
        with open("f2.txt", "w") as f:
            self.preOrder2(self.root, f)
            print("")
    def preOrder2(self, p, f):
        if p == None:
            return
        if p.data.Price <= 5 and p.data.Price >= 3:
            self.visit2(p, f)
        self.preOrder2(p.left, f)
        self.preOrder2(p.right, f)
    def visit2(self,p, f):
        if p == None:
            return
        f.write(f"{p.data}")

        pass
        #end def
    
    def f2_1(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2=======
        with open("f2.txt", "w") as f:
            self.postOrder(self.root, f)
            print("")
    def postOrder(self,p, f):
        if p==None:
            return
        self.postOrder(p.left, f)
        self.postOrder(p.right, f)
        if p.data.Price <= 5 and p.data.Price >= 3:
            self.visit2(p) 
    def visit2(self,p, f):
        if p == None:
            return
        f.write(f"{p.data}")
        #end def
        
    def f2_1_1(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2=======
        with open("f2.txt", "w") as f:
            self.inOrder(self.root, f)
            print("")
    def inOrder(self,p, f):
        if p==None:
            return
        self.inOrder(p.left, f)
        if p.data.Price <= 5 and p.data.Price >= 3:
            self.visit2(p, f)
        self.inOrder(p.right, f)
        
    def visit2(self,p, f):
        if p == None:
            return
        f.write(f"{p.data}")
        
        pass
        #end def
    # ================================================================================= #
    # Nếu đề không yêu cầu gì -> mặc định là xoá trái.
    # Hãy cứ thử hết các hàm xoá trái/phải hoặc merging để check output nhá!
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========
        # Xoá con trai
        p = self.search_f3()
        self.delByCopyLeft(p)
        
    def search_f3(self): # Giành cho đề có 'BreathFirst search'
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.right and p.data.Price < 7: # Sửa điều kiện theo yêu cầu đề bài. Nếu y/c là kiểu số gì đó thì viết thành vd1: is square number -> is_square(p.data.Price) nhé! 
                count += 1
            if count == 1:  # Đề yêu cầu là node thứ mấy thì count bằng bấy nhiêu (ví dụ đề yêu cầu 'first node' thì count = 1)
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
        if node.data.Price < root.data.Price: #sửa theo đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
        #end def
        
    def delByCopyLeft(self,p):
        if not p:
            return
        rightmost = p.left
        parent = None
        while rightmost.right:
            parent = rightmost
            rightmost = rightmost.right
        p.data = rightmost.data
        if parent:
            parent.right = rightmost.left
        else:
            p.left = rightmost.left
        #end def
        pass
    #=============================================================================== #
    def f3_1(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========
        # Xoá con trái điều kiện là prime num
        p = self.search_f3()
        self.delByCopyLeft(p)
        self.delByCopyRight(p)
        
    def search_f3(self): # Giành cho đề có 'BreathFirst search'
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.right and self.is_prime(p.data.Price): # Sửa điều kiện theo yêu cầu đề bài. Nếu y/c là kiểu số gì đó thì viết thành vd1: is square number -> is_square(p.data.Price) nhé! 
                count += 1
            if count == 1:  # Đề yêu cầu là node thứ mấy thì count bằng bấy nhiêu (ví dụ đề yêu cầu 'first node' thì count = 1)
                return p
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        return None
    
    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Price < root.data.Price: #sửa theo đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
        #end def
        
    def delByCopyLeft(self,p):
        if not p:
            return
        rightmost = p.left
        parent = None
        while rightmost.right:
            parent = rightmost
            rightmost = rightmost.right
        p.data = rightmost.data
        if parent:
            parent.right = rightmost.left
        else:
            p.left = rightmost.left
        #end def
    def delByCopyRight(self,p):
        if not p:
            return
        leftmost = p.right
        parent = None
        while leftmost.left:
            parent = leftmost
            leftmost = leftmost.left
        p.data = leftmost.data
        if parent:
            parent.left = leftmost.rigt
        else:
            p.right = leftmost.right
        #end def
    #=============================================================================== #
    def f3_2(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========
        # Xoá by merging
        p = self.search_f3()
        #self.delByMergingLeft(p)
        #self.delByMergingRight(p)
        
    def search_f3(self): # Giành cho đề có 'BreathFirst search'
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.right and self.is_prime(p.data.Price): # Sửa điều kiện theo yêu cầu đề bài. Nếu y/c là kiểu số gì đó thì viết thành vd1: is square number -> is_square(p.data.Price) nhé! 
                count += 1
            if count == 1:  # Đề yêu cầu là node thứ mấy thì count bằng bấy nhiêu (ví dụ đề yêu cầu 'first node' thì count = 1)
                return p
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        return None
        #end def
    
    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
        #end def
    
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Price < root.data.Price: #sửa theo đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
        #end def
    
    def delByMergingLeft(self, node):
        parent = self._find_parent(self.root,node)
        if parent is None:
            self.root = node.left  
            self.insert_right_subtree(node.left, node.right)
        else:
            if parent.left == node:
                parent.left = node.left  
                self.insert_right_subtree(node.left, node.right)
            else:
                parent.right = node.left  
                self.insert_right_subtree(node.left, node.right)
        #end def
    
    def delByMergingRight(self, node):
        parent = self._find_parent(self.root, node)
        if parent is None:
            self.root = node.right  
            self.insert_left_subtree(node.left, node.right)
        else:
            if parent.left == node:
                parent.left = node.right  
                self.insert_left_subtree(node.left, node.right)
            else:
                parent.right = node.right  
                self.insert_left_subtree(node.left, node.right)
        #end def
    
    def insert_right_subtree(self, left_subtree, right_subtree):
        if left_subtree is None:
            return
        current = left_subtree
        while current.right:
            current = current.right
        current.right = right_subtree
        #end def
    
    def insert_left_subtree(self, left_subtree, right_subtree):
        if right_subtree is None:
            return
        current = right_subtree
        while current.left:
            current = current.left
        current.left = left_subtree
        #end def  
    #=============================================================================== #
    def post_order_search(self, node):
        if node is None:
            return None

        stack1 = []
        stack2 = []
        last_valid_node = None  # To store the last valid node

        stack1.append(node)

        while stack1:
            current = stack1.pop()
            stack2.append(current)

            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)

        while stack2:
            p = stack2.pop()
            if p.left is not None and p.right is not None and p.data.Age % 2 != 0:
                last_valid_node = p  # Update last_valid_node

        return last_valid_node  # Return the last valid node found
    #=============================================================================== #
    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========
        p = self.search_f4()
        self.rotate_right(p) #đề yêu cầu xoay bên phải
        
    def search_f4(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.data.Price < 7:
                count += 1
            if count == 1:                 
                return p
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        return None
        #end def
    
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Price < root.data.Price:   # Sửa 'data.' theo yêu cầu đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
        #end def
    
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
    #=============================================================================== #
    def f4_1(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========
        p = self.search_f4()
        self.rotate_right(p) #đề yêu cầu xoay bên phải
        
    def search_f4(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and self.is_prime(p.data.Price):
                count += 1
            if count == 1:                 
                return p
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        return None
        #end def
    
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Price < root.data.Price:   # Sửa 'data.' theo yêu cầu đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
        #end def
    
    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
        #end def
    
    def rotate_left(self, node):    
        if not node:                                            
            return None
        right_node = node.right                                 
        if not right_node:                                      
            return node
        right_left_node = right_node.left
        node.right = right_left_node                            
        right_node.left = node
        if node == self.root:                                   
            self.root = right_node
        else:                                                   
            parent = self._find_parent(self.root, node)         
            if parent.left == node:                             
                parent.left = right_node
            else:                                               
                parent.right = right_node
        return right_node
    #=============================================================================== #
    def f4_2(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4======== 
        p = self.search_f4()
        self.rotate_right(p) #đề yêu cầu xoay bên phải
        
    def search_f4(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and self.is_prime(p.data.Price):
                count += 1
            if count == 1:                 
                return p
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        return None
        #end def
    
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Price < root.data.Price:   # Sửa 'data.' theo yêu cầu đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
        #end def
    
    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
        #end def
    
    def rotate_left(self, node):    
        if not node:                                            
            return None
        right_node = node.right                                 
        if not right_node:                                      
            return node
        right_left_node = right_node.left
        node.right = right_left_node                            
        right_node.left = node
        if node == self.root:                                   
            self.root = right_node
        else:                                                   
            parent = self._find_parent(self.root, node)         
            if parent.left == node:                             
                parent.left = right_node
            else:                                               
                parent.right = right_node
        return right_node

        pass         
    #-----------------     