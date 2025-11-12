class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next, self.right.prev = self.right, self.left

    def remove_node_from_list(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def add_node_to_list(self, node):
        mru = self.right.prev
        mru.next, node.prev = node, mru
        self.right.prev, node.next = node, self.right
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node_from_list(node)
            self.add_node_to_list(node) # so it becomes the MRU
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update it
            node = self.cache[key]
            self.remove_node_from_list(node)
            node.value = value
            self.add_node_to_list(node)
        else:
            new_node = ListNode(key, value)
            self.add_node_to_list(new_node)
            self.cache[key] = new_node
            if len(self.cache) > self.capacity:
                lru = self.left.next
                del self.cache[lru.key]
                self.remove_node_from_list(lru)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
