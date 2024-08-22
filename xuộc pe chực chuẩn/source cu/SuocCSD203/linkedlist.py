class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")        
    
    def clear(self):
        self.head = None

    def addLast(self, name="", price=-1):
        if name.startswith("B") or price > 100:                      #add Last ,First có kiểm tra LL rỗng hay k
            return
        n = Node(Car(name, price))
        if (self.isEmpty()):
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def addFirst(self, name="", price=-1):
        if name.startswith("B") or price > 100:
            return
        n = Node(Car(name, price))
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head = n
            
    def AddAfterFirst(self, name, age):
        new_node=Node(data=Student(name,age))
        if self.head==None:
            self.head=new_node
            return
        cur = self.head
        while cur:
            if cur.data.Age % 2 == 0:
                new_node.next=cur.next
                cur.next=new_node
                break
            cur=cur.next
            
    def addAfterSecond(self, name, age):
        new_node = Node(data=Student(name,age))
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            curr=self.head
            prev=None
            count=0
            while curr:
                if curr.data.Age%2==0:
                    count +=1
                    if count == 2: #count bằng bao nhiêu thì thứ tự bấy nhiêu
                        newnode.next=curr.next
                        curr.next=newnode
                        break
                prev=curr
                curr=curr.next
            if curr is None and prev is not None:
                prev.next=new
                
    def addAfterLast(self, name, age):
        new_node=Node(Student(name,age))
        curr=self.head
        lastNode=None
        while curr:
            if curr.data.Age % 2 ==0:
                lastNode=curr
            curr=curr.next
        if lastNode is None:
            new_node.next=self.head
            self.head=new_node
        else:
            new_node.next=lastNode.next
            lastNode.next=new_node
        
    def addBeforeFirst(self, name, age):
        new_node=Node(data=Student(name,age))
        if not self.head or self.head.data.Age%2==0:
            new_node.next=self.head
            self.head=new_node
        else:
            curr=self.head
            prev=None
            while curr:
                if curr.data.Age%2==0:
                    if prev is None:
                        new_node.next=curr
                    else:
                        prev.next=new_node
                        new_node.next=curr
                    break
                prev=curr
                curr=curr.next
                
    def addBefore2nd(self, name, age):
        new_node=Node(data=Student(name, age))
        if not self.head or self.head.data.Age%2==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            prev=None
            count=0
            while current.next:
                if current.next.data.Age%2==0:
                    count+=1
                    prev=current
                    if count==2:
                        new_node.next=prev.next
                        prev.next=new_node
                        break
                current=current.next
                
    def addBeforeLast(self, name, age):
        new_node=Node(Student(name,age))
        curr=self.head
        prev=None
        lastNode=None
        while curr.next:
            if curr.next.data.Age%2==0: #even
                prev=curr
                lastNode=curr.next
            curr=curr.next
        if lastNode if None:#No node with even age found
            new_node.next=self.head
            self.head=new_node
        else:
            if lastNode==self.head:#last node is the head node
                new_node.next=self.head
                self.head=new_node
            else:
                prev.next=new_node
                new_node.next=lastNode
                
    def deleteFirstNode(self):
        if self.head is None:
            return
        #check if the first node's age is a square number
        if self.is_square(self.head.data.Age):
            self.head=self.head.next
            return
        current=self.head
        prev=None
        while current is not None:
            if self.is_square(current.data.Age):
                prev.next=current.next
                return
            prev=current
            current=current.next
        pass
    
    def delete2ndNode(self):
        if self.head is None:
            return
        count=0
        current = self.head
        prev=None
        while current is not None:
            if self.is_square(current.data.Age):
                count+=1
                if count==2:#count bằng bao nhiêu thì xóa thứ tự bấy nhiêu
                    prev.next=current.next
                    return
            prev=current
            current=current.next
            
    def deletelastNode(self):
        if self.head is None:
            return
        curr=self.head
        prev=None
        last_node=None
        while curr.next:
            if self.is_square(curr.next.data.Age):
                prev=curr
                last_node=curr.next
            curr =curr.next
        if last_node is not None:
            prev.next=last_node.next
            last_node.next=None
            
    def deleteMax(self):
        if not self.head:
            return
        #find the node with the maxium age
        max_age=self.head.data.Age
        max_age_node=self.head
        curr=self.head
        prev=None
        while curr.next:
            if curr.next.data.Age>max_age:
                max_age=curr.next.data.Age
                max_age_node=curr.next
                prev=curr
            curr=curr.next
        #Delete the node with maxium age
        if prev:
            prev.next=max_age_node.next
        else:
            self.head=max_age_node.next
        pass
    
    def delete2ndMax(self):
        if not self.head or self.head.next:
            return
        #find the maximun age node
        max_age=self.head.data.Age
        max_age_node=self.head
        curr=self.head
        prev=None
        while curr.next:
            if curr.next.data.Age>max_age:
                max_age=curr.next.data.Age
                max_age_node=curr.next
                prev=curr
            curr=curr.next
        #find the 2nd max age node
        second_max_age=self.head.data.Age
        second_max_age_node=self.head
        curr=self.head
        prev=None
        while curr.next:
            if curr.next.data.Age!=max_age and curr.next.data.Age>second_max_age:
                second_max_age=curr.next.data.Age
                second_max_age_node=curr.next
                prev=curr
            curr=curr.next
            
        if prev:
            prev.next=second_max_age_node.next
        else:
            self.head=second_max_age_node.next
        pass
    
    def deleteMin(self):
        if not self.head:
            return
        #find the min age node
        min_age=self.head.data.Age
        min_age_node=self.head
        curr=self.head
        prev=None
        
        while curr.next:
            if curr.next.data.Age<min_age:
                min_age=curr.next.data.Age
                min_age_node=curr.next
                prev=curr
            curr=curr.next
            
        #delete the min age node
        if prev:
            prev.next=min_age_node.next
        else:
            self.head=min_age_node.next
            
    def delete2ndMin(self):
        if self.head is None or self.head.next is None:
            return
        #find the 2nd min age
        min1=self.head.data.Age
        min2=math.inf
        curr=self.head
        while curr is not None:
            if curr.data.Age<min1:
                min2=min1
                min1=curr.data.Age
            elif min1<curr.data.Age<min2:
                min2=curr.data.Age
            curr=curr.next
            
        #delete the node with 2nd min age
        curr=self.head
        prev=None
        while curr is not None:
            if curr.data.Age==min2:
                if prev if None:
                    self.head=curr.next
                else:
                    prev.next=curr.next
                break
            prev=curr
            curr=curr.next
            
    def sort(self):
        ls2=[]
        cur=self.head
        while cur:
            if not self.is_fibonacci_number(cur.data.Age):
                lst2.append((cur.data.Name, cur.data.Age))
            cur=cur.next
        
        lst2.sort(key=lamda x: x[1])
        
        j = 0
        cur = self.head
        while cur:
            if not self.is_fibonacci_number(cur.data.Age):
                cur.data.Name, cur.data.Age=lst2[j]
                j+=1
            cur=cur.next
    
    def sort(self):#sort with index
        totalNode=self.count()
        
        lst2=[]
        lst2=[]
        cur=self.head  
        for i in range(totalNode):
                lst2.append((cur.data.Name, cur.data.Salary))
            cur=cur.next
            
        lst2=sorted(lst2 , key=lamda x: x[1], reverse=True)
        j=0
        cur=self.head
        for i in range(totalNode):
            if i%2==1:
                cur.data.Name=lst2[j][0]
                cur.data.Salary=lst2[j][i]
            cur=cur.next
            cur=cur.next
    
    def count(self):
        cur=self.head
        count=0
        while cur:
            count+=1
            cur=cur.next
        return count
        
        

    def delete(self, price=0):
        if self.isEmpty():
            return
        prev_node = None
        curr_node = self.head
        last_node_with_price = None
        last_prev_node = None
        while curr_node:
            if curr_node.data.Price == price: #thay ĐK
                last_node_with_price = curr_node
                last_prev_node = prev_node
            prev_node = curr_node
            curr_node = curr_node.next

        if last_node_with_price:
            if last_node_with_price == self.head:
                self.head = self.head.next
            else:
                last_prev_node.next = last_node_with_price.next
                if last_node_with_price == self.tail:
                    self.tail = last_prev_node
Xóa giá trị giống nhau cuối