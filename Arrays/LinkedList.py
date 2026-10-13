class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Create original nodes
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

# Connect original list
node1.next = node2
node2.next = node3
node3.next = node4

# Establish the head
head = node1


# Insert 2 at the beginning
new_node = Node(2)

new_node.next = head
head = new_node


# Traverse
current = head

while current is not None:
    print(current.value)
    current = current.next

