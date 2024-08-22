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