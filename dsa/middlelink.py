class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


# Find middle
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next


print("Middle node:", slow.data)