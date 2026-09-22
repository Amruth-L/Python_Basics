class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

# Connect the nodes
head.next = second
second.next = third
third.next = fourth

# Create a cycle:
# 40 → 20
fourth.next = second


# Detect cycle
slow = head
fast = head

cycle_found = False

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        cycle_found = True
        break


if cycle_found:
    print("Cycle exists")
else:
    print("No cycle")