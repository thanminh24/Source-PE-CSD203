import math
from Student import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")        
    def clear(self):
        self.head = None
#Q1-1
    def addFirst(self, name="", age=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if name[0] == "X" or age < 10: #sửa điều kiện theo yêu cầu đề bài
            return
        new_node = Node(Student(name, age))
        new_node.next = self.head
        self.head = new_node        
        pass
    # end def
    def addLast(self, name, age):
        if name[-1] != 'Z' and age <= 120:#sửa điều kiện theo yêu cầu đề bài
            return
        n = Node(Student(name,age))
        if (self.isEmpty()):
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
##########################################################
    def addAfterFirst(self, name, age):
        new_node = Node(data=Student(name, age))
        if self.head == None:
            self.head = new_node
            return
        cur = self.head
        while cur:
            if cur.data.Age % 2 == 0:#sửa điều kiện theo yêu cầu đề bài
                new_node.next = cur.next
                cur.next = new_node
                break
            cur = cur.next
    def addAfterSecond(self, name, age):
        newnode = Node(data = Student(name, age))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            curr = self.head
            prev = None
            count = 0
            while curr:
                if curr.data.Age % 2 == 0:#sửa điều kiện theo yêu cầu đề bài
                    count += 1
                    if count == 2: #count bằng bao nhiêu thì thứ tự bấy nhiêu
                        newnode.next = curr.next
                        curr.next = newnode
                        break
                prev = curr
                curr = curr.next
            if curr is None and prev is not None:
                prev.next = new
    def addAfterLast(self, name, age):
        new_node = Node(Student(name,age))
        curr = self.head
        lastNode = None
        while curr:
            if curr.data.Age % 2 == 0:#sửa điều kiện theo yêu cầu đề bài
                lastNode = curr
            curr= curr.next
        if lastNode is None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = lastNode.next
            lastNode.next = new_node
    def addBeforeFirst(self, name, age):
        new_node = Node(data = Student(name, age))
        if not self.head or self.head.data.Age % 2 == 0:#sửa điều kiện theo yêu cầu đề bài
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev = None
            while curr:
                if curr.data.Age % 2 == 0:#sửa điều kiện theo yêu cầu đề bài
                    if prev is None:
                        new_node.next = curr
                    else:
                        prev.next = new_node
                        new_node.next = curr
                    break
                prev = curr
                curr = curr.next
    def addBefore2nd(self, name, age):
        new_node = Node(data=Student(name, age))

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            prev = None
            count = 0
            while current:
                if current.data.Age % 2 == 0:#sửa điều kiện theo yêu cầu đề bài
                    count += 1
                    if count == 2:#count bằng bao nhiêu, thứ tự bấy nhiêu
                        new_node.next = current
                        if prev:
                            prev.next = new_node
                        else:
                            self.head = new_node
                        break
                prev = current
                current = current.next
    def addBeforeLast(self, name, age):
        new_node = Node(Student(name, age))
        curr = self.head
        prev = None
        lastNode = None
        while curr.next:
            if curr.next.data.Age % 2 == 0:#sửa điều kiện theo yêu cầu đề bài
                prev = curr
                lastNode = curr.next
            curr = curr.next
        if lastNode is None:  # No node with even age found
            new_node.next = self.head
            self.head = new_node
        else:
            if lastNode == self.head:  # Last node is the head node
                new_node.next = self.head
                self.head = new_node
            else:
                prev.next = new_node
                new_node.next = lastNode
#########Delete node
    def deleteFirstNode(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ========
        if self.head is None:
            return
        # Check if the first node's age is a square number
        if self.is_square(self.head.data.Age):
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current is not None:
            if self.is_square(current.data.Age):#sửa điều kiện theo yêu cầu đề bài
                prev.next = current.next
                return
            prev = current
            current = current.next
        pass    
    def delete2ndNode(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ========
        if self.head is None:
            return
        count = 0
        current = self.head
        prev = None
        while current is not None:
            if self.is_square(current.data.Age):#sửa điều kiện theo yêu cầu đề bài
                count += 1
                if count == 2: #count bằng bao nhiêu xoá thứ tự bấy nhiê
                    prev.next = current.next
                    return
            prev = current
            current = current.next
    def deleteLastNode(self):
        if self.head is None:
            return
        curr = self.head
        prev = None
        last_node = None
        while curr.next:
            if self.is_square(curr.next.data.Age):#sửa điều kiện theo yêu cầu đề bài
                prev = curr
                last_node = curr.next
            curr = curr.next
        if last_node is not None:
            prev.next = last_node.next
            last_node.next = None
        
    def deleteMax(self):
        if not self.head:
            return

        # Find the node with the maximum age
        max_age = self.head.data.Age
        max_age_node = self.head
        curr = self.head
        prev = None

        while curr.next:
            if curr.next.data.Age > max_age:
                max_age = curr.next.data.Age
                max_age_node = curr.next
                prev = curr
            curr = curr.next

        # Delete the node with the maximum age
        if prev:
            prev.next = max_age_node.next
        else:
            self.head = max_age_node.next

        pass
    def delete2ndMax(self):
        if not self.head or not self.head.next:
            return

        # Find the maximum age node
        max_age = self.head.data.Age
        max_age_node = self.head
        curr = self.head
        prev = None

        while curr.next:
            if curr.next.data.Age > max_age:
                max_age = curr.next.data.Age
                max_age_node = curr.next
                prev = curr
            curr = curr.next

        # Find the second maximum age node
        second_max_age = self.head.data.Age
        second_max_age_node = self.head
        curr = self.head
        prev = None

        while curr.next:
            if curr.next.data.Age != max_age and curr.next.data.Age > second_max_age:
                second_max_age = curr.next.data.Age
                second_max_age_node = curr.next
                prev = curr
            curr = curr.next

        # Delete the second maximum age node
        if prev:
            prev.next = second_max_age_node.next
        else:
            self.head = second_max_age_node.next

        pass
    def deleteMin(self):
        if not self.head:
            return

        # Find the minimum age node
        min_age = self.head.data.Age
        min_age_node = self.head
        curr = self.head
        prev = None

        while curr.next:
            if curr.next.data.Age < min_age:
                min_age = curr.next.data.Age
                min_age_node = curr.next
                prev = curr
            curr = curr.next

        # Delete the minimum age node
        if prev:
            prev.next = min_age_node.next
        else:
            self.head = min_age_node.next

        pass
    def delete2ndMin(self):
        if self.head is None or self.head.next is None:
            return

        # Find the second minimum age
        min1 = self.head.data.Age
        min2 = math.inf
        curr = self.head
        while curr is not None:
            if curr.data.Age < min1:
                min2 = min1
                min1 = curr.data.Age
            elif min1 < curr.data.Age < min2:
                min2 = curr.data.Age
            curr = curr.next

        # Delete the node with the second minimum age
        curr = self.head
        prev = None
        while curr is not None:
            if curr.data.Age == min2:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                break
            prev = curr
            curr = curr.next
    def deleteAll(self):
        if self.head is None:
            return

        # Check if the first node's age is a square number
        while self.head is not None and self.is_square(self.head.data.Age):
            self.head = self.head.next

        current = self.head
        prev = None
        while current is not None:
            if self.is_square(current.data.Age):
                if prev is not None:
                    prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        pass
##########4 Sort
    def sort(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4pass
        lst2 = []
        cur = self.head
        while cur:
            if not self.is_fibonacci_number(cur.data.Age):
                lst2.append((cur.data.Name, cur.data.Age))
            cur = cur.next

        lst2.sort(key=lambda x: x[1])  # Sorting lst2 in ascending order based on age

        j = 0
        cur = self.head
        while cur:
            if not self.is_fibonacci_number(cur.data.Age):
                cur.data.Name, cur.data.Age = lst2[j]
                j += 1
            cur = cur.next
## Sort with index
    def sort(self):
        totalNode = self.count()
        
        lst2 = []
        cur = self.head
        for i in range(totalNode):
            if i % 2 == 1:
                lst2.append((cur.data.Name, cur.data.Salary))
            cur = cur.next
        
        lst2 = sorted(lst2, key = lambda x: x[1], reverse=True)# Sorting lst2 in ascending order based on age
                                                        #x[1], -ord(x[0][0]) tuổi tăng dần, tên giảm dần
                                                        #-x[1], x[0] tuổi giảm, tên tăng
        j = 0
        cur = self.head
        for i in range(totalNode):
            if i % 2 == 1:
                cur.data.Name = lst2[j][0]
                cur.data.Salary = lst2[j][1]
                j += 1
            cur = cur.next
    def count(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            
        return count