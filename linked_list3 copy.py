class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            print('This is a new node via prepend method:', self.head.value)
        new_node.next = self.head
        self.head = new_node
        print(f'added {self.head.value} via prepend')
        print(f'the next node is {self.head.next.value}')
        
            
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print('Head Node Created:', self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next
        
        node.next = new_node
        print(f'the new node is {node.next.value}')

llist = LinkedList() 
llist.append('Frist')
llist.append('sec')
llist.append('3')
llist.prepend('fake node')   

