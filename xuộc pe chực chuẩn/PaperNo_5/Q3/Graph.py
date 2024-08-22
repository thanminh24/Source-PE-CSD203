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
    def deg(self, x):
        count =0
        for i in range(len(self.a)):
            count += self.a[x][i]
        return count      
    # end
           
    def f1(self,start):      # start is a character such as 'A'  
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
   
       

        
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




        pass
    
               
                                     