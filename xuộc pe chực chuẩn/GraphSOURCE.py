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
    #----------------------------
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
        print(f"{chr(start+65)}({t})", end = " ")    
        for i in range(len(b)):
            if self.a[start][i]!=0 and b[i]:
                b[i] = False
                self.depth2(i,b)
######
    def breadth_first(self,start):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        x = self.char_to_number(start)
        b = [True] * len(self.a)
        b[x] = False
        self.breadth(x, b)
        for i in range(len(b)):
            if b[i]:
                b[i] = False
                self.breadth(i, b)
    
    def breadth(self, start, b):
        queue = MyQueue()
        queue.EnQueue(start)
        while not queue.isEmpty():
            v = queue.DeQueue()
            print(f"{chr(v + 65)}", end=" ")

            for i in range(len(b)):
                if self.a[v][i] != 0 and b[i]:
                    b[i] = False
                    queue.EnQueue(i)

    def char_to_number(self, char):
        return ord(char.upper()) - 65


        #---------------------------
    
    
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
    def Euler(self,start):
        #===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        stack = Stack()
        euler_cycle = []

        stack.push(start)

        while not stack.isEmpty():
            r = stack.top()

            if self.isIsolated(r):
                stack.pop()
                euler_cycle.append(chr(r + 65))
            else:
                for y in range(len(self.a)):
                    if self.a[r][y] != 0:
                        stack.push(y)
                        self.a[r][y] = 0
                        self.a[y][r] = 0
                        break
        
        print(' '.join(euler_cycle))
    
    def isIsolated(self, vertex):
        for y in range(len(self.a)):
            if self.a[vertex][y] != 0:
                return False
        return True
    ##################
    def Euler(self, start):#if start is char
    # Convert character to integer
    start = ord(start) - 65

    # Rest of the code remains the same
    stack = Stack()
    euler_cycle = []

    stack.push(start)

    while not stack.isEmpty():
        r = stack.top()

        if self.isIsolated(r):
            stack.pop()
            euler_cycle.append(chr(r + 65))
        else:
            for y in range(len(self.a)):
                if self.a[r][y] != 0:
                    stack.push(y)
                    self.a[r][y] = 0
                    self.a[y][r] = 0
                    break
    
    print(' '.join(euler_cycle))

def isIsolated(self, vertex):
    for y in range(len(self.a)):
        if self.a[vertex][y] != 0:
            return False
    return True



        #------------------------------
        print("")
        

    # -----------------------------
    def Dsk(self,start,end): #dành cho start = num ( "1")
        num_vertices = len(self.a)
        dist = [math.inf] * num_vertices
        dist[start] = 0

        queue = MyQueue()
        queue.EnQueue(start)

        while not queue.isEmpty():
            u = queue.DeQueue()

            for v in range(num_vertices):
                if self.a[u][v] != 0:
                    new_dist = dist[u] + self.a[u][v]
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        queue.EnQueue(v)

        path = self.getShortestPath(start, end, dist)
        shortest_distances = ' '.join([str(dist[i]) for i in path])
        shortest_path = ' '.join([chr(vertex + 65) for vertex in path])

        print(shortest_path)
        print(shortest_distances)
    
    def getShortestPath(self, start, end, dist):
        path = [end]
        curr = end

        while curr != start:
            for v in range(len(self.a)):
                if self.a[curr][v] != 0:
                    if dist[curr] - self.a[curr][v] == dist[v]:
                        path.append(v)
                        curr = v
                        break

        return path[::-1]
    def DJK(self,start,end): #dành cho start = char("A")
        num_vertices = len(self.a)
        dist = [math.inf] * num_vertices
        dist[self.char_to_number(start)] = 0

        queue = MyQueue()
        queue.EnQueue(self.char_to_number(start))

        while not queue.isEmpty():
            u = queue.DeQueue()

            for v in range(num_vertices):
                if self.a[u][v] != 0:
                    new_dist = dist[u] + self.a[u][v]
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        queue.EnQueue(v)

        path = self.getShortestPath(self.char_to_number(start), self.char_to_number(end), dist)

        if path:
            shortest_path = '-'.join([chr(vertex + 65) for vertex in path])
            shortest_distances = '-'.join([f"{chr(vertex + 65)}({dist[vertex]})" for vertex in path[::-1]])
        else:
            shortest_path = "No path"
            shortest_distances = "No path"

        print(shortest_path)
        print(shortest_distances)
    def getShortestPath(self, start, end, dist):
        path = [end]
        curr = end

        while curr != start:
            for v in range(len(self.a)):
                if self.a[curr][v] != 0:
                    if dist[curr] - self.a[curr][v] == dist[v]:
                        path.append(v)
                        curr = v
                        break

        return path[::-1]

