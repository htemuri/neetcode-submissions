class LinkNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        buckets = 10000
        self.hashmap = [LinkNode(0, 0) for _ in range(buckets)]

    def put(self, key: int, value: int) -> None:
        hkey = key % len(self.hashmap)
        cur = self.hashmap[hkey]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = LinkNode(key, value)

    def get(self, key: int) -> int:
        hkey = key % len(self.hashmap)
        cur = self.hashmap[hkey]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        hkey = key % len(self.hashmap)
        cur = self.hashmap[hkey]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)