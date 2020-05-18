class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:

    def __init__(self):
        self.start = None

    def insert_last(self, value):
        newnode = Node(value)
        if self.start is None:
            self.start = newnode
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode

    def view(self):
        temp = self.start
        while temp:
            print(temp.data, end=("-->"))
            if temp.next is None:
                break
            temp = temp.next

a = linked_list()
a.insert_last(10)
a.insert_last(11)
a.insert_last(20)
a.view()


