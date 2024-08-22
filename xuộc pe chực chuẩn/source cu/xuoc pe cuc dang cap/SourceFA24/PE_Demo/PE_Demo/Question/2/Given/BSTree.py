import math
from Product import *
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
    def insert(self,name, price):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        newNode = Node(data = Product(name, price))
        if name[0] == "G" or  price < 0:
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
    def f2(self):        
       # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2=======
       self.inOrder2(self.root)
       print("")
       pass
    def inOrder2(self,p):
        if p==None:
            return
        h = self.height(p)
        self.inOrder2(p.left)
        if p.data.Price % 2 != 0:
            print(f"{p.data}({h})",end =" ")
        self.inOrder2(p.right)  
        pass
    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1
    def f3(self):
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 
        node = self.search_f3()
        self.delByMergingLeft(node)
    def search_f3(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and self.is_fibonacci_number( p.data.Price):
            #Sửa điều kiện theo yêu cầu đề bài
                count += 1
            if count == 2:
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
        if node.data.Price < root.data.Price: #sửa theo đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
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

    def insert_right_subtree(self, left_subtree, right_subtree):
        if left_subtree is None:
            return
        current = left_subtree
        while current.right:
            current = current.right
        current.right = right_subtree
    # def delByCopyLeft(self,p):
    #     if not p:
    #         return
    #     rightmost = p.left
    #     parent = None
    #     while rightmost.right:
    #         parent = rightmost
    #         rightmost = rightmost.right
    #     p.data = rightmost.data
    #     if parent:
    #         parent.right = rightmost.left
    #     else:
    #         p.left = rightmost.left
    #     pass
    def is_fibonacci_number(self,num):
            if num < 0:
                return False
            a, b = 0, 1
            while b < num:
                a, b = b, a + b
            return b == num 
    
    def f4(self):
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========
        node = self.search_f4()
        self.rotate_left(node)
        
    def search_f4(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.right and self.isPerfectNumber(p.data.Price):
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
        if node.data.Price < root.data.Price:
        #Sửa data. theo yêu cầu đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
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
    def isPerfectNumber(self,num):
        if num <= 0:
            return False
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        
        return divisors_sum == num


# end class
