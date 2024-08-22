import math
from Stack import *
from MyQueue import *
class Graph:
    def __init__(self,data):
        self.a = data
    def display(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                print(self.a[i][j], end =" ")
            print("")
        print("")
    def depthFirst(self,start):
        b = [True] * len(self.a)
        #gán các đỉnh chưa được đi qua là True
        b[start] = False
        #Bắt đầu di chuyển các đỉnh được đi qua gán là False
        self.depth(start,b)
        for i in range(len(b)):
        #Kiểm tra các đỉnh còn lại đã được đi qua chưa
            if b[i]:
                b[i] = False
                self.depth(i,b)
    def depth(self,start,b):
        t = self.deg(start)
        #Tìm bậc của từng đỉnh
        print(f"{chr(start+65)}", end = " ")
        #chr(65) = A
        for i in range(len(b)):
            if self.a[start][i]!=0 and b[i]:
                b[i] = False
                self.depth(i,b)
    def deg(self, x):
        count =0
        for i in range(len(self.a)):
            count += self.a[x][i]
        return count     
    # end
           
    def f1(self,start):
        self.depthFirst(start)
        print("")
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1========
        self.depthFirst2(start)
        print("")
    def depthFirst2(self,start):
        b = [True] * len(self.a)
        b[start] = False    
        self.depth2(start,b)
        for i in range(len(b)):
            if b[i]:
                b[i] = False
                self.depth2(i,b)
    def depth2(self,start,b):
        t = self.deg(start)
        if t %2 != 0: 
            print(f"{chr(start+65)}[{t}]", end = " ")
        else:
            print(f"{chr(start+65)}", end = " ")
        for i in range(len(b)):
            if self.a[start][i]!=0 and b[i]:
                b[i] = False
                self.depth2(i,b)
        pass
    #------------------------------
    def f2(self, start):  # start is a character such as 'A'       
              
        self.Euler(start)
        
        pass     
    def Euler(self,start):
        '''declare a stack S of characters
            declare empty array E (which will contain Euler cycle)
            push the vertex X to S
            while(S is not empty):
                r = top element of the stack S 
                if r is isolated then:
                    remove it from the stack and put it to E
                else
                    select the first vertex Y (by alphabet order), which is adjacent
                    to r, push  Y  to  S and remove the edge (r,Y) from the graph 
            the last array E obtained is an Euler cycle of the graph'''       
       
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========   
        # Convert character to integer
        start=ord(start)-65 # nếu như start là chữ cái 

        degree_dict= self.depthFirst3(start)

        if self.checkEuler()==False:
            return
        S=Stack()
        E=[]
        S.push(start)
        while  not S.isEmpty():
            r=S.top()
            if self.deg(r)==0:
                S.pop()
                E.append(chr(r+65))
            else:
                y=None
                for i in range(len(self.a[r])):
                    if self.a[r][i]!=0:
                        if y is None or i<y:
                            y=i
                S.push(y)
                self.a[r][y]-=1
                self.a[y][r]-=1
        print(' '.join(E))
        # In chu trình Euler với các đỉnh có bậc nhỏ hơn 6
        for e in E:
            if e in degree_dict and degree_dict[e]<6:
                print(f'{e}[{degree_dict[e]}]',end=" ")
            else:
                print(e,end=" ")
        print()
        
    # tính và trả về bậc của từng đỉnh thành một dictionary
    def depthFirst3(self,start):
        degree_dict={}
        b = [True]*len(self.a)
        b[start] = False    
        self.depth3(start,b,degree_dict)
        for i in range(len(b)):
            if b[i]:
                b[i] = False
                self.depth3(i,b,degree_dict)
        return degree_dict
                
    def depth3(self,start,b,degree_dict):
        t = self.deg(start)
        degree_dict[f"{chr(start+65)}"]=t
        for i in range(len(b)):
            if self.a[start][i]!=0 and b[i]:
                b[i] = False
                self.depth3(i,b,degree_dict)

    def checkConnectivity(self):
        CanVisit = [True]*len(self.a)
        CanVisit[0]=False
        self.depth_traversal(0,CanVisit)
        for i in range(len(self.a)):
            if CanVisit[i]==True:
                return False
        return True

    def checkEuler(self):
        if not self.checkConnectivity():
            return False
        for i in range(len(self.a)):
            if self.deg(i)%2!=0:
                return False
        return True

    def depth_traversal(self,p,CanVisit): # duyệt đồ thị liên kết và không liên kết
        for i in range(len(self.a)):
            if CanVisit[i] and self.a[i][p]!=0:
                CanVisit[i]=False
                self.depth_traversal(i,CanVisit)
        # print(' '.join(E[::-1]))

               
                                     