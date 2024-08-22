from BSTree import *
import re
class Main:
    def __init__(self,fileName):
        self.fileName = fileName
        self.data = None
    #end def    
    def readFile(self, lineStart, numberline):
        f1 = open(self.fileName,'r');
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count== lineStart+1:                
                # listName = re.sub("\s+"," ",line.strip()).split(",")   
                listName = line.strip().split(",")             
                self.data =[listName];
            if count>lineStart+1 and count<lineStart+1+numberline: 
                # listValue = re.sub("\s+"," ",line.strip()).split(",")
                listValue = line.strip().split(",")
                self.data.append(listValue)
        f1.close()
    def display(self):
        for line in self.data:
            print(line, end ="\n")        
                # listName = line.strip().split(", ")
    def insert(self, tree):
        for i in range(len(self.data[0])):           
            tree.f1(self.data[0][i].strip(),int(self.data[1][i].strip()),int(self.data[2][i]))
    #end def       
    def createTree(self,tree,begin=0, end=0):
        self.readFile(begin, end)
        for i in range(len(self.data[0])):
            tree.f1(self.data[0][i].strip(),int(self.data[1][i].strip()),int(self.data[2][i]))
#####################            
m = Main("input.txt")
tree = BSTree()
print("1. Test f1 (1 mark)")
print("2. Test f2 (1 mark)")
print("3. Test f3 (1 mark)")
print("4. Test f4 (1 mark)")
choice = int(input("Your selection (1->4)"))
print("OUTPUT")
if choice ==1:    
    m.readFile(1,3)
    m.insert(tree)
    tree.preVisit()    
    tree.breadth_first()    
elif choice ==2:
    tree.clear()
    m.createTree(tree,5,3)
    tree.preVisit()
    tree.f2()
elif choice ==3:
    tree.clear()
    m.createTree(tree,9,3)   
    tree.postVisit()
    tree.f3()
    tree.postVisit()    
elif choice==4:
    tree.clear()
    m.createTree(tree,13,3)
    tree.breadth_first()    
    tree.f4()
    tree.breadth_first()
else:
    print("Wrong select")
print("FINISH")    