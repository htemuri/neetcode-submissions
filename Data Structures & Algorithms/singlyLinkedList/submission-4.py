class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        curr = self.head
        for i in range(index):
            if not curr.next:
                return -1
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head
        self.head = newHead

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        # scroll to last node
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head
        for i in range(index - 1):
            print("currval", curr.val, ":", curr.next)
            if not curr.next:
                print("condition")
                return False
            curr = curr.next
        if not curr.next:
            print("condition")
            return False
        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        vals = []
        if not self.head:
            return []
        curr = self.head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        return vals
