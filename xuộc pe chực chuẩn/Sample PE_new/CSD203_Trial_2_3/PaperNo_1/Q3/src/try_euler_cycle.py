class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

class Graph:
    def __init__(self, matrix):
        self.a = matrix

    def deg(self, vertex):
        return sum(self.a[vertex])

    def f2(self,start):
        #===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        if self.checkEuler()==False:
            return
        mystack=Stack()
        e=[]
        mystack.push(start)
        while  not mystack.isEmpty():
            r=mystack.top()
            if self.deg(r)==0:
                mystack.pop()
                e.append(chr(r+65))
            else:
                y=None
                for i in range(len(self.a[r])):
                    if self.a[r][i]!=0:
                        if y is None or i<y:
                            y=i
                mystack.push(y)
                self.a[r][y]-=1
                self.a[y][r]-=1
        print(' '.join(e))

        print(' '.join(e[::-1]))

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
def main():
    # Ví dụ bạn đưa ra:
    matrix = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
        
    ]

    g = Graph(matrix)
    start_vertex = 0  # Bắt đầu từ đỉnh 0 (tức là A)
    g.f2(start_vertex)

if __name__ == "__main__":
    main()
