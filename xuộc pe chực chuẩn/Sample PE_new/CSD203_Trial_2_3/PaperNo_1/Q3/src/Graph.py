import math
from Stack import *
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
        b = [True]*len(self.a)
        b[start] = False    
        self.depth(start,b)
        for i in range(len(b)):
            if b[i]:
                b[i] = False
                self.depth(i,b)

    def depth(self,start,b):
        t = self.deg(start)
        print(f"{chr(start+65)}", end = " ")    
        for i in range(len(b)):
            if self.a[start][i]!=0 and b[i]:
                b[i] = False
                self.depth(i,b)

    def deg(self, x):
        count =0
        for i in range(len(self.a)):
            count += self.a[x][i]
        return count
    #----------------------------
    def f1(self,start):
        
        print("")
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1========
        self.depthFirst2(start)
    def depthFirst2(self,start):
        b = [True]*len(self.a)
        b[start] = False    
        self.depth2(start,b)
        for i in range(len(b)):
            if b[i]:
                b[i] = False
                self.depth2(i,b)
                
    def depth2(self,start,b):
        t = self.deg(start)
        print(f"{chr(start+65)}({t})", end = " ")    
        for i in range(len(b)):
            if self.a[start][i]!=0 and b[i]:
                b[i] = False
                self.depth2(i,b)


        #---------------------------
        print("")
    
    #----------------------------    
    '''Algorithm for finding an Euler cycle from the vertex X using stack 
//Input: Connected graph G with all vertices having even degrees
//Output: Euler cycle
declare a stack S of characters
declare empty array E (which will contain Euler cycle)
push the vertex X to S
while(S is not empty)
 {r = top element of the stack S 
  if r is isolated then remove it from the stack and put it to E
   else
   select the first vertex Y (by alphabet order), which is adjacent
   to r, push  Y  to  S and remove the edge (r,Y) from the graph   
 }
 the last array E obtained is an Euler cycle of the graph'''
    #-------------------------------------
    def f2(self,start):
        #===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
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

        print(' '.join(E[::-1]))
        
        for e in E:
            t=self.deg(e)
            if  t<6:
                print(f'{e}[{t}]')
            else:
                print(f'{e}')


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
        #------------------------------
    
        print("")