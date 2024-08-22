from MyList import *
from Employee import *
class Main:
    def __init__(self,fileName):
        self.fileName = fileName
        self.data = None
        self.obj = None
    #end def   
    def q2(self, lineStart):
        f1 = open(self.fileName,'r')
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count == lineStart +1:
                self.obj = line
                break              
        pass 
    def readFile(self, lineStart, numberline):
        f1 = open(self.fileName,'r');
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count== lineStart+1:
                listName = line.strip().split(", ")
                self.data =[listName];
            if count>lineStart+1 and count<lineStart+1+numberline: 
                listValue = line.strip().split(", ")
                self.data.append(listValue)
        f1.close()
    def display(self):
        for line in self.data:
            print(line, end ="\n")        
                # listName = line.strip().split(", ")
    def addFirst(self, linkList):
        for i in range(len(self.data[0])):
            linkList.f1(self.data[0][i].strip(),int(self.data[1][i].strip()),int(self.data[2][i]))
    #end def       
    def creatList(self,linkList,begin=0, end=0):
        self.readFile(begin, end)
        for i in range(len(self.data[0])):
            linkList.f1(self.data[0][i].strip(),int(self.data[1][i].strip()),int(self.data[2][i]))
#####################            
m = Main("input.txt")
linkList = MyList()
print("1. Test f1 (1 mark)")
print("2. Test f2 (1 mark)")
print("3. Test f3 (1 mark)")
print("4. Test f4 (1 mark)")
choice = int(input("Your selection (1->4)"))
print("OUTPUT")
if choice ==1:    
    m.readFile(1,3)
    m.addFirst(linkList)
    linkList.traverse()
elif choice ==2:
    linkList.clear()
    m.q2(5)
    x = m.obj.strip().split(", ")
    emp = Employee(x[0],x[1],int(x[2]))
    m.creatList(linkList,6,3)
    linkList.traverse()
    linkList.f2(emp)
    linkList.traverse()
elif choice ==3:
    linkList.clear()
    m.creatList(linkList,10,3)   
    linkList.traverse() 
    linkList.f3()
    linkList.traverse()
elif choice==4:
    linkList.clear()
    #m.q2(14)
    m.creatList(linkList,15,3)
    linkList.traverse()
    linkList.f4()
    linkList.traverse()
else:
    print("Wrong select")
print("FINISH")    