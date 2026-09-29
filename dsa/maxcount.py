class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



head = Node(10)
head.next = Node(20)
head.next.next = Node(10)
head.next.next.next = Node(30)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(40)



target = 10


count = 0
current = head

while current:
    if current.data == target:
        count += 1

    current = current.next


print(target, "appears", count, "times")