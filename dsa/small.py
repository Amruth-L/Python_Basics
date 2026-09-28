class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None(25)
head.next=None(10)
head.next.next=None(-20)
head.next.next.next=None(-40)
smallest = head.data
current = head.next

while current:
    if current.data < smallest:
        smallest = current.data

    current = current.next


print("Smallest:", smallest)