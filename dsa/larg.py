class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


head=Node(10)
head.next=Node(25)
head.next.next=Node(7)
head.next.next.next=Node(40)
head.next.next.next.next=Node(18)

largest=head.data
current=head.next

while current:
    if current.data > largest:
        largest=current.data

    current=current.next
print("Largest",largest)