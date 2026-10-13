class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


#create the 4 nodes
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

# Connect the nodes
node1.next = node2
node2.next = node3
node3.next = node4
head = node1

while head is not None:
    print(head.value)
    head = head.next

