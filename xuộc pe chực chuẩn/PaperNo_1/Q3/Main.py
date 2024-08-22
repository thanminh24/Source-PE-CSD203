from Graph import *
import re
class Main:
    def __init__(self,fileName):
        self.fileName = fileName
        self.data = []
        self.lineNumber =0
        self.obj = None
    #end def    
    def f(self,lineStart):
        f1 = open(self.fileName,'r');
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count== lineStart:
                self.obj = line                
                break   
    def readFile(self, lineStart):
        f1 = open(self.fileName,'r');
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count== lineStart:
                lineNumber = int(line)                
                for i in range(lineNumber): 
                    line = f1.readline()                    
                    listValue = re.sub("\\s+"," ",line.strip()).split(" ")                
                    row =[]
                    for j in range(len(listValue)):                        
                        row.append(int(listValue[j]))
                    self.data.append(row)
        f1.close()
        for i in range (len(self.data)):
            for j in range(i,len(self.data)):
                self.data[j][i] = self.data[i][j]
    def display(self):
        for line in self.data:
            [print(x, end=" ") for x in line]   
            print()     
                # listName = line.strip().split(", ")
    def clear(self):
        self.data =[]
        self.lineNumber = 0
    
#####################            
m = Main("input.txt")
print("1. Test f1 (1 mark)")
print("2. Test f2 (1 mark)")
choice = int(input("Your selection (1->2)"))
print("OUTPUT")
if choice ==1:  
    m.f(2)
    start = ord(m.obj.strip())-65
    m.readFile(3)
    # m.display()
    g = Graph(m.data)
    g.f1(start)
elif choice ==2:
    m.clear()
    m.f(3)  
    start = int(m.obj)
    m.f(3+start+2)
    # start = ord(m.obj.strip())-65
    para =re.sub("\\s+"," ",m.obj.strip()).split(" ")    
    m.readFile(3+start+3)
    g = Graph(m.data)
    g.f2(para[0])    
else:
    print("Wrong select")
print("FINISH")    