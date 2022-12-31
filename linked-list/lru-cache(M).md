# Intuition
The most immense pain that you could imagine

# Approach
The idea here is that we store each key-value pair as a node in a doubly linked list. The node closest to the head is the least recently used node, and the node closest to the tail is the most recently used node. We keep a hashmap storing each key, where the value references the actual node stored in the linked list. In our solution, we store a hashmap, a current and max capacity, and a reference to our doubly linked list class. A breakdown of the functions are as follows:

- get(key): If the key we're looking for isn't in the hashmap, return -1. Otherwise, this key needs to become the most recently used. To do this, delete the old node from the linked list, and create a new node with the exact same key-value pair and insert it at the end of the list. Update the reference to this new node in the hashmap

- put(key, value): 
    - If the key we're trying to add already exists, update the val stored in the node, delete the old node from the linked list, and create a new node with the key value pair at the end of the list since it's the most recently used. Update the reference to this new node in the hashmap
    - If the key doesn't exist, but we're at max capacity, we delete the least recently used node and add the new node at the end. We first get the key of the least recently used node, and delete it from the hashmap. Then we delete the old node from the list, and add the new node at the end. Finally, create the reference to this new node in the hashmap
    - If the key doesn't exist, and we're not at max capacity, create the new node and add it to the list, and create the reference to this new node in the hashmap

# Complexity
- Time complexity: Both functions are $O(1)$, which is the reason behind the doubly linked list
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(capacity)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.curr_capacity = 0
        self.max_capacity = capacity
        self.linked_list = DoublyLinkedList(capacity)

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        new_node = self.linked_list.update(self.hashmap[key])
        self.hashmap[key] = new_node
        return new_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            new_node = self.linked_list.update(node)
            self.hashmap[key] = new_node

        elif self.curr_capacity == self.max_capacity:
            del self.hashmap[self.linked_list.getLeastRecentNodeKey()]
            new_node = self.linked_list.put(key, value)
            self.hashmap[key] = new_node

        else:
            new_node = self.linked_list.put(key, value)
            self.hashmap[key] = new_node
            self.curr_capacity += 1

class DoublyLinkedList:

    def __init__(self, max_capacity: int):

        self.max_capacity = max_capacity
        self.curr_capacity = 0
        self.head = self.Node(0, 0, None, None)
        self.tail = self.Node(0, 0, None, None)

        self.head.nxt = self.tail
        self.tail.prev = self.head

    def getLeastRecentNodeKey(self) -> int:
        return self.head.nxt.key

    def update(self, node):
        self.remove(node)
        return self.put(node.key, node.val)

    def put(self, key: int, val: int):

        if self.curr_capacity == self.max_capacity:
            self.remove(self.head.nxt)
            return self.put(key, val)
        else:
            new_node = self.Node(key, val, None, None)
            end_node = self.tail.prev

            end_node.nxt = new_node
            new_node.prev = end_node
            new_node.nxt = self.tail
            self.tail.prev = new_node

            self.curr_capacity += 1
            return new_node
        
    def remove(self, node) -> None:
        prev_node = node.prev
        next_node = node.nxt

        prev_node.nxt = next_node
        next_node.prev = prev_node

        self.curr_capacity -= 1

    class Node:
        def __init__(self, key: int, val: int, prev, nxt):
            self.key = key
            self.val = val
            self.prev = prev
            self.nxt = nxt
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
