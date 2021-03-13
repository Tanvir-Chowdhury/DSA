class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:

    def __init__(self):
        self.start = None
        self.size = 0

    def insert_first(self, value):
        newnode = Node(value)
        if self.start is None:
            self.start = newnode
        else:
            temp = self.start
            newnode.next = temp
            self.start = newnode
        self.size += 1

    def insert_any(self, value, e):
        newnode = Node(value)
        if self.start is None:
            self.start = newnode
        else:
            temp = self.start
            for i in range(1, e-1):
                temp = temp.next
            newtemp = temp
            newnode.next = temp.next
            newtemp.next = newnode
        self.size += 1    

    def insert_last(self, value):
        newnode = Node(value)
        if self.start is None:
            self.start = newnode
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
        self.size += 1
    
    def delete_first(self):
        if self.size == 0:
            print("list is empty")
        else:
            temp = self.start
            self.start = temp.next
        self.size -= 1

    def delete_any(self, e):
        if self.size == 0:
            print("list is empty")
        else:
            temp = self.start
            for i in range(1, e-1):
                temp = temp.next
            temp.next = temp.next.next

    def delete_last(self):
        if self.size == 0:
            print("list is empty")
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def view(self):
        temp = self.start
        while temp:
            print(temp.data, end=("-->"))
            if temp.next is None:
                break
            temp = temp.next

a = linked_list()
a.insert_first("Tanvir")
a.insert_first("Sifat")
a.insert_first(70)
a.insert_last(10)
a.insert_last(11)
a.insert_last(20)
a.insert_any(100, 3)
a.delete_first()
a.delete_last()
a.delete_any(3)
a.view()


