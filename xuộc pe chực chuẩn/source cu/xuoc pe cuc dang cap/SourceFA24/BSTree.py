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



######################################################### 
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        p = self.search_f3() 
        #self.delByCopyLeft(p) #Nếu đề ko yêu cùng dùng left hay right thì thường là dùng left
        self.delByMergingLeft(p)#Nếu đề ko yêu cùng dùng left hay right thì thường là dùng left
        
    
    def search_f3(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.right and p.data.Price < 7:
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
##############Delete by Copy                
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
###Delete by copy select right child           
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
######## Delete by Merging
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Age < root.data.Age: #sửa theo đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
#####Delete by Merging select left child         
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

        pass
###Delte by merging select right child  
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
    def insert_left_subtree(self, left_subtree, right_subtree):
        if right_subtree is None:
            return

        current = right_subtree
        while current.left:
            current = current.left

        current.left = left_subtree
####################################################################           
            
    def f4(self):
    #  ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        p = self.search_f4()
        self.rotate_right(p) #đề yêu cầu xoay bên nào thì xoay bên đấy
    def search_f4(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.data.Price < 7:
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

    #################################
        pass
# Kết thúc dạng đề PeFa22
######################################################################
#Các dạng có thể gặp
#Height và balance factor
    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1 #Trả về giá trị height của node được truyền vào
    def balanceFactor(self, node): 
        rightHeight = self.height(node.right)
        leftHeight = self.height(node.left)
        return (rightHeight - leftHeight)#Trả về giá trị balance factor của node được truyền vào

#Đề yêu cầu in cây theo chiều postOrder cùng với chiều cao hoặc balance factor của nó
    def f2(self):        
       # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2========
        self.postOrder2(self.root)
        print("")
    def postOrder2(self,p):
    #Nếu đề yêu cầu preOrder hoặc inOrder hoặc breath_first copy lại preOrder hoặc inOrder hoặc breath_first có sẵn bên trên và đổi tên
        if p==None:
            return
        self.postOrder2(p.left)
        self.postOrder2(p.right)
        # if:.... theo đề bài yêu cầu, dòng này luôn đừng trước self.visit (nếu có nhớ self.visit phải thụt lề)
        self.visit2(p)
    def visit2(self,p):
        if p==None:
            return
        h = self.height(p) # đề yêu cầu chiều cao
        #b = self.balanceFactor # đề yêu cầu balance factor
        print(f"{p.data}({h})",end =" ")
#Nhớ phải copy hàm balanceFactor hoặc Height
    
#Đề yêu cầu in cây cùng với level của nó
    def postOrder2(self,p,level = 1):
        if p==None:
            return
        self.postOrder2(p.left, level + 1)
        self.postOrder2(p.right, level + 1)
        # if:.... theo đề bài yêu cầu, dòng này luôn đừng trước self.visit (nếu có nhớ self.visit phải thụt lề)
        print(f"{p.data}({level})",end =" ") # thay thế self.visit
        # Nếu đề yêu cầu in theo thứ tự khác, copy hàm thứ tự mà đề yêu câu sửa tên và sửa phần visit
# Đề yêu cầu in ra cùng với level
    def postOrder2(self,p, level = 1):
        if p==None:
            return
        self.postOrder2(p.left)
        self.postOrder2(p.right)
        if p.data.Age % 2 != 0:
            print(f"{p.data} ({level + 1})",end =" ")
#Tìm giá trị lớn nhất, nhỏ nhất
#Tìm max
    def find_max_age_node(self):
        if not self.root:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr
# Tìm min
    def find_min_age_node(self):
        if not self.root:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr
#Tìm giá trị lớn nhất, nhỏ nhất thứ 2
#Tìm 2nd max
    def find_second_max_age_node(self):
        if self.root is None or (self.root.left is None and self.root.right is None):
            return None
        
        parent = None
        current = self.root
        
        while current.right is not None:
            parent = current
            current = current.right
        
        if current.left is not None:
            current = current.left
            
            while current.right is not None:
                current = current.right
                
            return current
        else:
            return parent
#tìm 2nd min
    def find_second_min_age_node(self):
        if self.root is None or (self.root.left is None and self.root.right is None):
            return None
        
        parent = None
        current = self.root
        
        while current.left is not None:
            parent = current
            current = current.left
        
        if current.right is not None:
            current = current.right
            
            while current.left is not None:
                current = current.left
                
            return current
        else:
            return parent
    
