class Node:
    def __init__(self, key):
        self.val = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.keys = [Node(-1) for i in range(10000)]
        
    def add(self, key: int) -> None:
        curr = self.keys[key % len(self.keys)]
        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = Node(key)
        

    def remove(self, key: int) -> None:
        curr = self.keys[key % len(self.keys)]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next
          
    def contains(self, key: int) -> bool:
        curr = self.keys[key % len(self.keys)]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False




# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)